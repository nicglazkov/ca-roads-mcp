# Eval results

Generated 2026-07-10T21:12:25+00:00 by `evals/run_evals.py` from `v1.13.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 18/28 (64%) | 19/28 (68%) |
| quiet-day | 19/30 (63%) | 22/30 (73%) |
| real-2026-07-07 | 3/6 (50%) | 3/6 (50%) |
| storm-day | 15/27 (56%) | 17/27 (63%) |
| **all** | 55/91 (60%) | 61/91 (67%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 1/4 (25%) | 2/4 (50%) |
| `check_route` | 11/18 (61%) | 12/18 (67%) |
| `get_chain_controls` | 16/20 (80%) | 14/20 (70%) |
| `get_incidents` | 8/15 (53%) | 10/15 (67%) |
| `get_lane_closures` | 9/19 (47%) | 11/19 (58%) |
| `get_wildfires` | 10/15 (67%) | 12/15 (80%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 29 | claude-haiku-4-5 / fire-i5-why: Failed to report the VULCAN fire closure, incorrectly claiming I-5 is open with no incidents. |
| hallucinated-event | 21 | claude-haiku-4-5 / quiet-101-closures: Correctly reports the Trimble Rd closure but invents a second closure (Story Rd on-ramp) not in the... |
| other | 8 | claude-haiku-4-5 / fire-route-la-sac: Correctly identifies I-5 Grapevine closure and VULCAN fire, but says only northbound closed (truth... |
| stale-data-trust | 4 | claude-haiku-4-5 / quiet-i80-closures: Claims the feed is unavailable and misses the actual shoulder-only litter removal record near Davis. |
| bad-refusal | 2 | claude-haiku-4-5 / fire-sr17: The assistant asked for clarification instead of reporting that SR-17 has no incidents, closures,... |
| wrong-tool-or-no-tool | 2 | claude-sonnet-5 / quiet-i80-closures: The assistant claimed no data was available due to a feed outage instead of reporting the... |

## Tool selection

21/176 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.99**
