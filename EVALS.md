# Eval results

Generated 2026-07-10T08:44:12+00:00 by `evals/run_evals.py` from `v1.12.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 14/28 (50%) | 21/28 (75%) |
| quiet-day | 22/30 (73%) | 20/30 (67%) |
| real-2026-07-07 | 1/6 (17%) | 3/6 (50%) |
| storm-day | 15/27 (56%) | 16/27 (59%) |
| **all** | 52/91 (57%) | 60/91 (66%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 2/4 (50%) | 2/4 (50%) |
| `check_route` | 10/18 (56%) | 9/18 (50%) |
| `get_chain_controls` | 15/20 (75%) | 16/20 (80%) |
| `get_incidents` | 10/15 (67%) | 11/15 (73%) |
| `get_lane_closures` | 6/19 (32%) | 9/19 (47%) |
| `get_wildfires` | 9/15 (60%) | 13/15 (87%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 34 | claude-haiku-4-5 / fire-i5-why: The assistant claims I-5 is not closed, contradicting the active VULCAN fire closure in both... |
| hallucinated-event | 25 | claude-haiku-4-5 / fire-i5-open: Conveys the closure correctly but invents a specific VULCAN wildfire cause not in the ground truth. |
| other | 7 | claude-haiku-4-5 / fire-route-la-sac: Says only northbound closed (ground truth: both directions) and omits the SR-99 alternative. |
| bad-refusal | 2 | claude-haiku-4-5 / quiet-i80-closures: The assistant refused with a data-unavailable claim instead of reporting that there are no lane... |
| stale-data-trust | 1 | claude-haiku-4-5 / quiet-place-davis: It admits the lane closure feed failed rather than confirming the shoulder-only closure, so it... |
| wrong-location | 1 | claude-haiku-4-5 / storm-lowest-elevation-control: It cites Echo Summit near Mile 57 rather than the correct R-1 at Pollock Pines and R-2 at Twin... |

## Tool selection

27/177 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.94**
