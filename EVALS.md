# Eval results

Generated 2026-07-11T01:11:55+00:00 by `evals/run_evals.py` from `v2.4.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 17/28 (61%) | 21/28 (75%) |
| quiet-day | 19/30 (63%) | 20/30 (67%) |
| real-2026-07-07 | 2/6 (33%) | 3/6 (50%) |
| storm-day | 15/27 (56%) | 15/27 (56%) |
| **all** | 53/91 (58%) | 59/91 (65%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 2/4 (50%) | 3/4 (75%) |
| `check_route` | 8/18 (44%) | 12/18 (67%) |
| `get_chain_controls` | 14/20 (70%) | 14/20 (70%) |
| `get_incidents` | 10/15 (67%) | 8/15 (53%) |
| `get_lane_closures` | 8/19 (42%) | 10/19 (53%) |
| `get_wildfires` | 11/15 (73%) | 12/15 (80%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 31 | claude-haiku-4-5 / fire-i5-open: Claims southbound is passable, but ground truth says I-5 is fully closed in both directions at the... |
| hallucinated-event | 23 | claude-haiku-4-5 / fire-alt-check: Correctly steers away from closed I-5 and recommends CA-99, but invents a wildfire and Fresno... |
| other | 11 | claude-haiku-4-5 / fire-i15: judge output unparseable |
| bad-refusal | 3 | claude-haiku-4-5 / fire-99-alternative: The assistant asked for origin/destination instead of reporting the SR-99 lane closure at 7th... |
| wrong-tool-or-no-tool | 1 | claude-haiku-4-5 / fire-remote: The assistant asked for location instead of providing the known answer that REMOTE is not... |
| stale-data-trust | 1 | claude-sonnet-5 / storm-freshness: Chain conditions match the ground truth but the timestamps are contradictory and appear... |

## Tool selection

22/178 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.88**
