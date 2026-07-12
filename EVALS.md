# Eval results

Generated 2026-07-12T21:11:54+00:00 by `evals/run_evals.py` from `v2.20.1`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-sonnet-4-6` (not an evaluated model).

## Scorecard

| Scenario | `claude-sonnet-5` |
|---|---|
| fire-day | 20/28 (71%) |
| quiet-day | 21/30 (70%) |
| real-2026-07-07 | 3/6 (50%) |
| storm-day | 18/27 (67%) |
| **all** | 62/91 (68%) |

## Pass rate by tool

| Tool | `claude-sonnet-5` |
|---|---|
| `check_region` | 1/4 (25%) |
| `check_route` | 11/18 (61%) |
| `get_chain_controls` | 15/20 (75%) |
| `get_incidents` | 13/15 (87%) |
| `get_lane_closures` | 8/19 (42%) |
| `get_wildfires` | 14/15 (93%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| hallucinated-event | 16 | claude-sonnet-5 / fire-alt-check: The answer contradicts ground truth by claiming I-5 southbound is open and recommending it as the... |
| missed-active-condition | 9 | claude-sonnet-5 / fire-i5-open: Answer correctly identifies northbound closure and the Frazier Mountain Park Rd closure but hedges... |
| bad-refusal | 2 | claude-sonnet-5 / fire-99-alternative: The assistant refused to answer and asked for clarification instead of providing the known SR-99... |
| other | 2 | claude-sonnet-5 / fire-chains: Answer correctly states no chain controls but omits the key context that it's fire season with all... |

## Tool selection

13/90 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.55**
