# Eval results

Generated 2026-07-12T20:58:33+00:00 by `evals/run_evals.py` from `v2.20.0`. Models answer the golden questions using the MCP tool surface served from recorded fixtures; grading is exact-fact matching plus an LLM judge scored against ground truth. Judge: `claude-sonnet-4-6` (not an evaluated model).

## Scorecard

| Scenario | `claude-sonnet-5` |
|---|---|
| fire-day | 23/28 (82%) |
| quiet-day | 22/30 (73%) |
| real-2026-07-07 | 2/6 (33%) |
| storm-day | 19/27 (70%) |
| **all** | 66/91 (73%) |

## Pass rate by tool

| Tool | `claude-sonnet-5` |
|---|---|
| `check_region` | 2/4 (50%) |
| `check_route` | 12/18 (67%) |
| `get_chain_controls` | 15/20 (75%) |
| `get_incidents` | 13/15 (87%) |
| `get_lane_closures` | 9/19 (47%) |
| `get_wildfires` | 15/15 (100%) |

## Failure taxonomy

| Category | Count | Example |
|---|---|---|
| hallucinated-event | 12 | claude-sonnet-5 / quiet-101-closures: The answer correctly identifies the Trimble Rd closure but halluccinates an additional northbound... |
| missed-active-condition | 8 | claude-sonnet-5 / fire-i5-open: Answer incorrectly states southbound is not closed, contradicting the ground truth that both... |
| bad-refusal | 3 | claude-sonnet-5 / fire-99-alternative: The assistant asked for clarification instead of providing the known SR-99 closure at 7th Standard... |
| other | 1 | claude-sonnet-5 / fire-chains: Answer correctly states no chain controls but misses the key contextual detail that it's fire... |
| stale-data-trust | 1 | claude-sonnet-5 / quiet-sr1-bigsur: The assistant undermines the correct no-closure status by citing a data gap and warning of possible... |

## Tool selection

10/90 answers led with a different tool than the golden question targets (declared vs first observed call). Not always an error - check_region can legitimately answer a get_incidents question - but a rising rate means the tool descriptions are drifting.

Mean answer quality (judge, 1-5): **3.74**
