# Eval results

Generated 2026-07-12T01:01:09+00:00 by `evals/run_evals.py` from `v2.12.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 15/28 (54%) | 19/28 (68%) |
| quiet-day | 22/30 (73%) | 18/30 (60%) |
| real-2026-07-07 | 2/6 (33%) | 4/6 (67%) |
| storm-day | 16/27 (59%) | 16/27 (59%) |
| **all** | 55/91 (60%) | 57/91 (63%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 3/4 (75%) | 2/4 (50%) |
| `check_route` | 11/18 (61%) | 10/18 (56%) |
| `get_chain_controls` | 14/20 (70%) | 16/20 (80%) |
| `get_incidents` | 11/15 (73%) | 8/15 (53%) |
| `get_lane_closures` | 7/19 (37%) | 9/19 (47%) |
| `get_wildfires` | 9/15 (60%) | 12/15 (80%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 30 | claude-haiku-4-5 / fire-i5-open: Claims southbound is passable, but ground truth says both directions are fully closed at the... |
| hallucinated-event | 25 | claude-haiku-4-5 / fire-incidents-grapevine: The NB item was a traffic hazard, not a full closure, so the answer invents closure details and... |
| other | 10 | claude-haiku-4-5 / quiet-one-way-84: judge output unparseable |
| bad-refusal | 3 | claude-haiku-4-5 / quiet-i80-closures: The assistant refused to answer citing an unavailable feed instead of reporting there are no lane... |
| wrong-location | 1 | claude-haiku-4-5 / storm-lowest-elevation-control: Answer names Echo Summit rather than the correct R-1 at Pollock Pines and R-2 at Twin Bridges. |
| stale-data-trust | 1 | claude-sonnet-5 / storm-placerville-not-established: Answer claims a data outage and refuses to answer, contradicting the ground truth that a... |

## Tool selection

26/176 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.87**
