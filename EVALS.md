# Eval results

Generated 2026-07-11T22:43:19+00:00 by `evals/run_evals.py` from `v2.10.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-opus-4-8` (not an evaluated model).

## Scorecard

| Scenario | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| fire-day | 16/28 (57%) | 21/28 (75%) |
| quiet-day | 19/30 (63%) | 23/30 (77%) |
| real-2026-07-07 | 2/6 (33%) | 4/6 (67%) |
| storm-day | 15/27 (56%) | 16/27 (59%) |
| **all** | 52/91 (57%) | 64/91 (70%) |

## Pass rate by tool

| Tool | `claude-haiku-4-5` | `claude-sonnet-5` |
|---|---|---|
| `check_region` | 2/4 (50%) | 3/4 (75%) |
| `check_route` | 10/18 (56%) | 13/18 (72%) |
| `get_chain_controls` | 14/20 (70%) | 16/20 (80%) |
| `get_incidents` | 11/15 (73%) | 10/15 (67%) |
| `get_lane_closures` | 9/19 (47%) | 8/19 (42%) |
| `get_wildfires` | 6/15 (40%) | 14/15 (93%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| missed-active-condition | 31 | claude-haiku-4-5 / fire-i5-why: The assistant reported no closure when the VULCAN fire had fully closed I-5 at the Grapevine. |
| hallucinated-event | 25 | claude-haiku-4-5 / quiet-101-closures: Correctly reports the Trimble Rd closure but invents a second Story Rd On-Ramp closure not in... |
| other | 7 | claude-haiku-4-5 / fire-tahoe-chains: judge output unparseable |
| bad-refusal | 2 | claude-haiku-4-5 / fire-99-alternative: The assistant asked for more info instead of reporting the SR-99 lane closure at 7th Standard Rd. |
| wrong-tool-or-no-tool | 1 | claude-sonnet-5 / storm-placerville-not-established: Assistant claims the closure feed is down and refuses to answer, but ground truth shows the... |

## Tool selection

21/177 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.96**
