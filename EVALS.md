# Eval results

Generated 2026-07-12T20:33:49+00:00 by `evals/run_evals.py` from `v2.19.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-sonnet-4-6` (not an evaluated model).

## Scorecard

| Scenario | `claude-sonnet-5` |
|---|---|
| fire-day | 21/28 (75%) |
| quiet-day | 22/30 (73%) |
| real-2026-07-07 | 2/6 (33%) |
| storm-day | 20/27 (74%) |
| **all** | 65/91 (71%) |

## Pass rate by tool

| Tool | `claude-sonnet-5` |
|---|---|
| `check_region` | 2/4 (50%) |
| `check_route` | 12/18 (67%) |
| `get_chain_controls` | 17/20 (85%) |
| `get_incidents` | 12/15 (80%) |
| `get_lane_closures` | 8/19 (42%) |
| `get_wildfires` | 14/15 (93%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| hallucinated-event | 15 | claude-sonnet-5 / fire-i5-open: The answer invents the 'VULCAN wildfire' (48,213 acres, 15% contained) and mentions unverified... |
| missed-active-condition | 6 | claude-sonnet-5 / fire-route-la-sac: Answer correctly identifies the I-5 Grapevine closure and Vulcan fire but fails to mention SR-99 as... |
| bad-refusal | 3 | claude-sonnet-5 / fire-99-alternative: The assistant refused to answer and asked for clarification instead of reporting the known SR-99... |
| other | 1 | claude-sonnet-5 / quiet-us50-watt: The answer correctly says US-50 is not closed but fails to mention the scheduled electrical work at... |
| wrong-location | 1 | claude-sonnet-5 / storm-kirkwood: Answer mentions R-2 at Kirkwood Meadows but misses the R-2 at Carson Pass, and incorrectly says... |

## Tool selection

11/90 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.62**
