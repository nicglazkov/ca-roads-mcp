# Eval results

Generated 2026-07-10T08:27:55+00:00 by `evals/run_evals.py` from `v1.11.1`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 15/28 (54%) | 20/28 (71%) |
| quiet-day | 21/30 (70%) | 19/30 (63%) |
| real-2026-07-07 | 2/6 (33%) | 4/6 (67%) |
| storm-day | 12/27 (44%) | 16/27 (59%) |
| **all** | 50/91 (55%) | 59/91 (65%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 1/4 (25%) | 2/4 (50%) |
| `check_route` | 11/18 (61%) | 10/18 (56%) |
| `get_chain_controls` | 14/20 (70%) | 16/20 (80%) |
| `get_incidents` | 10/15 (67%) | 10/15 (67%) |
| `get_lane_closures` | 7/19 (37%) | 10/19 (53%) |
| `get_wildfires` | 7/15 (47%) | 11/15 (73%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 35 | claude-haiku-4-5 / fire-i5-why: The assistant claims no closure exists when the VULCAN fire has fully closed both directions of I-5... |
| hallucinated-event | 29 | claude-haiku-4-5 / fire-i5-open: Invents a 'Vulcan wildfire' cause and hedges on the southbound closure that ground truth states is... |
| other | 5 | claude-haiku-4-5 / real-i80-closures: Reports 8 closures instead of 9 and mischaracterizes them all as construction, though it correctly... |
| bad-refusal | 3 | claude-haiku-4-5 / fire-99-alternative: The assistant asked for clarification instead of reporting the SR-99 closure at 7th Standard Rd. |
| stale-data-trust | 1 | claude-haiku-4-5 / quiet-place-davis: Claims all clear on lane closures despite the feed being unavailable, missing the shoulder-only... |

## Tool selection

25/174 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.87**
