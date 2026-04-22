from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.planner import planner
from agent.executor import executor

builder = StateGraph(AgentState)

builder.add_node("planner", planner)
builder.add_node("executor", executor)

# Entry point
builder.set_entry_point("planner")

# Flow: planner → executor
builder.add_edge("planner", "executor")

# ✅ CONDITIONAL LOOP (SAFE)
def should_continue(state):
    step = state["step"]
    plan = state["plan"]
    max_steps = state.get("max_steps", 5)

    # stop if plan finished
    if step >= len(plan):
        return False

    # stop if safety limit reached
    if step >= max_steps:
        return False

    return True

builder.add_conditional_edges(
    "executor",
    should_continue,
    {
        True: "executor",
        False: "__end__"
    }
)

graph = builder.compile()