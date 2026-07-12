# Eval results

Generated 2026-07-12T07:56:36+00:00 by `evals/run_evals.py` from `v2.15.2`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-sonnet-4-6` (not an evaluated model).

## Scorecard

| Scenario | `claude-sonnet-5` |
|---|---|
| fire-day | 24/28 (86%) |
| quiet-day | 22/30 (73%) |
| real-2026-07-07 | 3/6 (50%) |
| storm-day | 19/27 (70%) |
| **all** | 68/91 (75%) |

## Pass rate by tool

| Tool | `claude-sonnet-5` |
|---|---|
| `check_region` | 2/4 (50%) |
| `check_route` | 13/18 (72%) |
| `get_chain_controls` | 16/20 (80%) |
| `get_incidents` | 13/15 (87%) |
| `get_lane_closures` | 10/19 (53%) |
| `get_wildfires` | 14/15 (93%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| hallucinated-event | 14 | claude-sonnet-5 / quiet-101-closures: The Trimble Rd closure is correctly identified, but the assistant fabricates an additional... |
| missed-active-condition | 5 | claude-sonnet-5 / fire-route-sac-la-99: The answer omits the collision at Ming Ave near Bakersfield, which is an active condition mentioned... |
| bad-refusal | 3 | claude-sonnet-5 / fire-99-alternative: The assistant refused to answer and asked for clarification instead of providing the known SR-99... |
| other | 1 | claude-sonnet-5 / fire-chains: Answer correctly states no chain controls but omits the critical context that it's fire season and... |

## Tool selection

12/90 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.78**
