def run_agent(user_input):

    if not is_supported_task(user_input):
        return "⚠️ Currently I only support booking appointments and reminders."

    state = {
        "input": user_input,
        "plan": [],
        "step": 0,
        "result": "",
        "history": [],
        "max_steps": 5
    }

    result = graph.invoke(state, config={"recursion_limit": 20})

    return result["result"]
def is_supported_task(user_input):
    text = user_input.lower()

    # Only support these domains
    if any(word in text for word in ["doctor", "appointment", "meeting"]):
        return True

    return False