# Eval results

Generated 2026-07-12T06:00:13+00:00 by `evals/run_evals.py` from `v2.13.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 11/28 (39%) | 20/28 (71%) |
| quiet-day | 18/30 (60%) | 22/30 (73%) |
| real-2026-07-07 | 1/6 (17%) | 3/6 (50%) |
| storm-day | 15/27 (56%) | 16/27 (59%) |
| **all** | 45/91 (49%) | 61/91 (67%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 1/4 (25%) | 2/4 (50%) |
| `check_route` | 8/18 (44%) | 12/18 (67%) |
| `get_chain_controls` | 14/20 (70%) | 14/20 (70%) |
| `get_incidents` | 8/15 (53%) | 10/15 (67%) |
| `get_lane_closures` | 8/19 (42%) | 10/19 (53%) |
| `get_wildfires` | 6/15 (40%) | 13/15 (87%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 31 | claude-haiku-4-5 / fire-i5-open: Claims southbound is passable, but ground truth states I-5 is fully closed in both directions at... |
| hallucinated-event | 23 | claude-haiku-4-5 / fire-when-reopen: The answer contradicts ground truth by claiming I-5 is open with no incidents, while the truth is... |
| other | 18 | claude-haiku-4-5 / fire-all-fires: judge output unparseable |
| bad-refusal | 4 | claude-haiku-4-5 / fire-99-alternative: The assistant asked for clarification instead of reporting the SR-99 closure at 7th Standard Rd. |

## Tool selection

28/176 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.80**
