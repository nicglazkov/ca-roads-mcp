# Eval results

Generated 2026-07-17T01:31:01+00:00 by `evals/run_evals.py` from `v2.22.1`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-sonnet-4-6` (not an evaluated model).

## Scorecard

| Scenario | `claude-sonnet-5` |
|---|---|
| fire-day | 22/28 (79%) |
| quiet-day | 19/30 (63%) |
| real-2026-07-07 | 2/6 (33%) |
| storm-day | 19/27 (70%) |
| **all** | 62/91 (68%) |

## Pass rate by tool

| Tool | `claude-sonnet-5` |
|---|---|
| `check_region` | 2/4 (50%) |
| `check_route` | 8/18 (44%) |
| `get_chain_controls` | 16/20 (80%) |
| `get_incidents` | 11/15 (73%) |
| `get_lane_closures` | 11/19 (58%) |
| `get_wildfires` | 14/15 (93%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| hallucinated-event | 17 | claude-sonnet-5 / fire-incidents-grapevine: The answer correctly mentions the traffic hazard on I-5 NB and road closure on I-5 SB, but... |
| missed-active-condition | 7 | claude-sonnet-5 / fire-route-sac-la-99: Answer omits the collision at Ming Ave near Bakersfield, which is an active condition a driver... |
| other | 3 | claude-sonnet-5 / fire-chains: Answer correctly states no chain controls but omits the key ground-truth context that it's fire... |
| bad-refusal | 2 | claude-sonnet-5 / fire-99-alternative: The assistant refused to answer and asked for clarification instead of providing the known SR-99... |

## Tool selection

12/90 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.60**
