"""CAL FIRE active incidents from the public incidents.fire.ca.gov API.

Complements WFIGS: CAL FIRE posts its own incidents quickly (including
small fires below WFIGS's radar) but only covers what CAL FIRE responds
to. WFIGS stays the authoritative interagency base; this feed adds the
CAL FIRE incidents WFIGS does not list yet, deduplicated by name and
distance in merge_with_wfigs.

An earlier note in wildfire.py said this endpoint blocks non-browser
clients; verified 2026-07-10 that it serves plain JSON to any client.
"""

from __future__ import annotations

import contextlib
import re
from datetime import UTC, datetime

import httpx

from ca_roads.cache import TTLCache
from ca_roads.feeds import USER_AGENT
from ca_roads.geo import haversine_meters
from ca_roads.models import FeedResult, Wildfire

SOURCE = "calfire"
TTL_SECONDS = 5 * 60
MAX_SERVE_SECONDS = 60 * 60
TIMEOUT_SECONDS = 15.0

LIST_URL = "https://incidents.fire.ca.gov/umbraco/api/IncidentApi/List"

# Two fires are the same fire when their names normalize identically
# within this range, or when they sit almost on top of each other
# regardless of name. The spot radius must stay small: fire complexes
# put genuinely distinct fires 2-5 km apart (a 5 km radius collapsed
# 21 real WFIGS fires in live testing), while true cross-feed pairs
# with differing names sit within a few hundred meters.
SAME_NAME_METERS = 50_000.0
SAME_SPOT_METERS = 1_000.0


def normalize_fire_name(name: str) -> str:
    """'3-1 Pit Fire' -> '31PIT', 'RIDGE' -> 'RIDGE'.

    WFIGS names drop the word "Fire" and vary in punctuation; comparing
    alphanumerics with the suffix stripped matches the two feeds.
    """
    cleaned = re.sub(r"\s+fire\s*$", "", (name or "").strip(), flags=re.I)
    return re.sub(r"[^A-Z0-9]", "", cleaned.upper())


def parse_calfire_json(payload: list) -> list[Wildfire]:
    fires: list[Wildfire] = []
    for item in payload or []:
        if not isinstance(item, dict) or not item.get("IsActive"):
            continue
        if (item.get("Type") or "Wildfire") != "Wildfire":
            continue
        try:
            lat = float(item.get("Latitude") or 0)
            lon = float(item.get("Longitude") or 0)
        except (TypeError, ValueError):
            continue
        if not lat or not lon:
            continue
        discovered = None
        raw_started = item.get("Started") or ""
        with contextlib.suppress(ValueError):
            discovered = datetime.fromisoformat(
                raw_started.replace("Z", "+00:00")).astimezone(UTC)
        fires.append(Wildfire(
            id=f"calfire-{item.get('UniqueId') or ''}",
            name=(item.get("Name") or "").strip(),
            lat=lat,
            lon=lon,
            size_acres=item.get("AcresBurned"),
            percent_contained=item.get("PercentContained"),
            discovered_at=discovered,
        ))
    return fires


def _same_fire(a, b, spot_meters: float = SAME_SPOT_METERS) -> bool:
    meters = haversine_meters(a.lat, a.lon, b.lat, b.lon)
    return meters <= spot_meters or (
        meters <= SAME_NAME_METERS
        and normalize_fire_name(a.name) == normalize_fire_name(b.name))


def _dedupe(records: list) -> list:
    """Collapse WFIGS's own duplicates, first occurrence wins.

    Internal removal demands bulletproof evidence: the same normalized
    name, or literally the same point (<100 m - seen live as HILLTOP
    twice under two unit codes at identical coordinates). Anything
    looser starts deleting real fires: LA County lists distinct
    dispatch-numbered vegetation fires only 500-900 m apart."""
    kept: list = []
    for rec in records:
        if not any(_same_fire(rec, k, spot_meters=100.0) for k in kept):
            kept.append(rec)
    return kept


def merge_with_wfigs(wfigs: FeedResult, calfire: FeedResult) -> FeedResult:
    """Deduplicated WFIGS records plus the CAL FIRE incidents WFIGS
    does not have.

    WFIGS wins every duplicate: its records link to perimeter polygons
    and interagency identifiers. When WFIGS itself failed, CAL FIRE
    records still serve so the map is not blind to fire.
    """
    wfigs = FeedResult(
        source=wfigs.source, records=_dedupe(wfigs.records),
        data_as_of=wfigs.data_as_of, ok=wfigs.ok, stale=wfigs.stale,
        error=wfigs.error, notes=wfigs.notes,
    )
    if not calfire.ok or not calfire.records:
        if calfire.error:
            return FeedResult(
                source=wfigs.source, records=wfigs.records,
                data_as_of=wfigs.data_as_of, ok=wfigs.ok, stale=wfigs.stale,
                error=wfigs.error,
                notes=[*wfigs.notes, "CAL FIRE feed unavailable"],
            )
        return wfigs

    added = [cf for cf in calfire.records
             if not any(_same_fire(cf, wf) for wf in wfigs.records)]

    notes = list(wfigs.notes)
    if added:
        notes.append(f"{len(added)} additional fire(s) from CAL FIRE")
    if not wfigs.ok:
        notes.append("WFIGS unavailable; CAL FIRE records only")
    return FeedResult(
        source=wfigs.source,
        records=[*wfigs.records, *added],
        data_as_of=wfigs.data_as_of or calfire.data_as_of,
        ok=wfigs.ok or calfire.ok,
        stale=wfigs.stale,
        error=wfigs.error if not wfigs.ok and not calfire.ok else None,
        notes=notes,
    )


class CalFireSource:
    """Statewide cached fetcher, same cadence as WFIGS."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client
        self._cache = TTLCache()

    async def _fetch(self) -> list[Wildfire]:
        resp = await self._client.get(
            LIST_URL,
            params={"inactive": "false"},
            headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
            timeout=TIMEOUT_SECONDS,
        )
        resp.raise_for_status()
        return parse_calfire_json(resp.json())

    async def get(self) -> FeedResult:
        outcome = await self._cache.get(
            "ca", TTL_SECONDS, MAX_SERVE_SECONDS, self._fetch)
        if not outcome.served:
            return FeedResult(
                source=SOURCE, records=[], data_as_of=None, ok=False,
                error=outcome.error,
            )
        notes = ["live fetch failed; serving cached data"] if outcome.stale else []
        return FeedResult(
            source=SOURCE,
            records=list(outcome.value),
            data_as_of=outcome.fetched_at,
            stale=outcome.stale,
            ok=True,
            notes=notes,
        )
