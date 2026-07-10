# Eval results

Generated 2026-07-10T01:10:07+00:00 by `evals/run_evals.py` from `v1.10.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 13/28 (46%) | 24/28 (86%) |
| quiet-day | 19/30 (63%) | 19/30 (63%) |
| real-2026-07-07 | 2/6 (33%) | 5/6 (83%) |
| storm-day | 16/27 (59%) | 18/27 (67%) |
| **all** | 50/91 (55%) | 66/91 (73%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 2/4 (50%) | 2/4 (50%) |
| `check_route` | 9/18 (50%) | 12/18 (67%) |
| `get_chain_controls` | 14/20 (70%) | 15/20 (75%) |
| `get_incidents` | 9/15 (60%) | 11/15 (73%) |
| `get_lane_closures` | 10/19 (53%) | 11/19 (58%) |
| `get_wildfires` | 6/15 (40%) | 15/15 (100%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| hallucinated-event | 25 | claude-haiku-4-5 / quiet-101-closures: Invented a second closure (NB on-ramp at Story Rd) not in the ground truth. |
| missed-active-condition | 23 | claude-haiku-4-5 / fire-i5-why: The assistant reported I-5 as open, missing the VULCAN fire closure at the Grapevine. |
| other | 9 | claude-haiku-4-5 / fire-i15: judge output unparseable |
| stale-data-trust | 4 | claude-haiku-4-5 / quiet-sr17-clear: Claims no closures despite admitting the lane closure feed is unavailable, overstating certainty... |
| wrong-tool-or-no-tool | 2 | claude-haiku-4-5 / fire-remote: The assistant asked for location info instead of answering that REMOTE is in the Sierra away from... |
| bad-refusal | 2 | claude-haiku-4-5 / fire-sr17: Assistant asked for clarification instead of stating that SR-17 has no incidents or closures. |
| wrong-location | 1 | claude-haiku-4-5 / quiet-route-sac-tahoe: US-50 corridor is in District 3, not District 10, so the stale-feed caveat references the wrong... |

## Tool selection

25/174 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.91**
