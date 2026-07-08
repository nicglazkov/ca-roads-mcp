# Eval results

Generated 2026-07-08T00:36:38+00:00 by `evals/run_evals.py` from `v1.2.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 13/28 (46%) | 19/28 (68%) |
| quiet-day | 20/30 (67%) | 22/30 (73%) |
| real-2026-07-07 | 3/6 (50%) | 4/6 (67%) |
| storm-day | 17/27 (63%) | 16/27 (59%) |
| **all** | 53/91 (58%) | 61/91 (67%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 2/4 (50%) | 1/4 (25%) |
| `check_route` | 11/18 (61%) | 10/18 (56%) |
| `get_chain_controls` | 13/20 (65%) | 16/20 (80%) |
| `get_incidents` | 10/15 (67%) | 9/15 (60%) |
| `get_lane_closures` | 8/19 (42%) | 12/19 (63%) |
| `get_wildfires` | 9/15 (60%) | 13/15 (87%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 29 | claude-haiku-4-5 / fire-i5-open: Correctly identifies NB Grapevine and SB Frazier closures but frames it as NB-only rather than a... |
| hallucinated-event | 23 | claude-haiku-4-5 / quiet-101-closures: Invented a second closure (NB on-ramp at Story Rd) not in the ground truth. |
| bad-refusal | 7 | claude-haiku-4-5 / fire-remote: The assistant refused to answer instead of stating that REMOTE is not threatening any major... |
| other | 5 | claude-haiku-4-5 / storm-chains-r2-meaning: R-2 requires chains installed on 2WD sedans, but the answer wrongly says you can keep driving... |
| wrong-tool-or-no-tool | 2 | claude-haiku-4-5 / fire-all-fires: The assistant refused to list the three active wildfires, claiming no statewide tool, instead of... |
| stale-data-trust | 2 | claude-haiku-4-5 / quiet-place-davis: The assistant claimed the Caltrans closure feed was unavailable and thus missed the shoulder-only... |

## Tool selection

24/169 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **4.00**
