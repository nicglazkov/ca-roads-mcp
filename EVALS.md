# Eval results

Generated 2026-07-09T23:12:20+00:00 by `evals/run_evals.py` from `v1.9.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 16/28 (57%) | 20/28 (71%) |
| quiet-day | 20/30 (67%) | 20/30 (67%) |
| real-2026-07-07 | 3/6 (50%) | 4/6 (67%) |
| storm-day | 13/27 (48%) | 17/27 (63%) |
| **all** | 52/91 (57%) | 61/91 (67%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 1/4 (25%) | 1/4 (25%) |
| `check_route` | 12/18 (67%) | 10/18 (56%) |
| `get_chain_controls` | 15/20 (75%) | 15/20 (75%) |
| `get_incidents` | 9/15 (60%) | 10/15 (67%) |
| `get_lane_closures` | 7/19 (37%) | 11/19 (58%) |
| `get_wildfires` | 8/15 (53%) | 14/15 (93%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 32 | claude-haiku-4-5 / fire-i5-why: The assistant claims I-5 is not closed, contradicting the active VULCAN fire closure. |
| hallucinated-event | 20 | claude-haiku-4-5 / fire-i5-open: Captures both closure locations but invents a VULCAN wildfire cause and understates the southbound... |
| other | 7 | claude-haiku-4-5 / storm-sr89-closure: The answer wrongly limits the full closure to southbound only, whereas the ground truth indicates a... |
| bad-refusal | 6 | claude-haiku-4-5 / fire-sr17: The assistant asked for clarification instead of reporting that SR-17 is clear. |
| stale-data-trust | 2 | claude-haiku-4-5 / quiet-place-davis: Claims lane-closure feed unavailable when ground truth shows a shoulder-only closure record exists... |
| wrong-location | 2 | claude-sonnet-5 / real-bay-area: States 14 total closures but ground truth says 37 lane closures with 4 ramp closures, a significant... |

## Tool selection

21/168 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.89**
