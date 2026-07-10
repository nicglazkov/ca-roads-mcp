# Eval results

Generated 2026-07-10T09:24:24+00:00 by `evals/run_evals.py` from `v1.12.1`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 16/28 (57%) | 20/28 (71%) |
| quiet-day | 19/30 (63%) | 20/30 (67%) |
| real-2026-07-07 | 3/6 (50%) | 4/6 (67%) |
| storm-day | 16/27 (59%) | 17/27 (63%) |
| **all** | 54/91 (59%) | 61/91 (67%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 2/4 (50%) | 2/4 (50%) |
| `check_route` | 13/18 (72%) | 12/18 (67%) |
| `get_chain_controls` | 13/20 (65%) | 15/20 (75%) |
| `get_incidents` | 11/15 (73%) | 9/15 (60%) |
| `get_lane_closures` | 7/19 (37%) | 9/19 (47%) |
| `get_wildfires` | 8/15 (53%) | 14/15 (93%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| hallucinated-event | 25 | claude-haiku-4-5 / fire-i5-open: Invents a specific wildfire cause and only reports northbound closure, missing the southbound... |
| missed-active-condition | 25 | claude-haiku-4-5 / fire-i5-why: The assistant claims I-5 is not closed, directly contradicting the active VULCAN fire closure. |
| other | 10 | claude-haiku-4-5 / fire-chains: judge output unparseable |
| bad-refusal | 3 | claude-haiku-4-5 / fire-99-alternative: The assistant asked for origin/destination instead of reporting the known SR-99 lane closure at 7th... |
| stale-data-trust | 3 | claude-haiku-4-5 / quiet-i80-closures: Correctly says no lane closures but falsely claims the feed is unavailable and omits the... |
| wrong-tool-or-no-tool | 1 | claude-sonnet-5 / quiet-i80-closures: The assistant claimed data was unavailable due to 404 errors rather than reporting the... |

## Tool selection

27/178 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.98**
