from utils.llm import call_llm

def planner(state):
    user_input = state["input"]

    prompt = f"""
    Break the task into steps ONLY if mentioned.

    Task: {user_input}

    Rules:
    - Do NOT add extra steps
    - Only include steps explicitly asked
    - If user only asks booking → return only booking
    - If user asks reminder → include reminder

    Example:
    Input: Book doctor
    Output:
    1. Book appointment

    Input: Book doctor and remind me
    Output:
    1. Book appointment
    2. Set reminder
    """

    response = call_llm(prompt)

    steps = []
    for line in response.split("\n"):
        line = line.strip()

        if not line:
            continue

        if "." in line:
            line = line.split(".", 1)[1].strip()

        steps.append(line)

    # fallback
    if len(steps) == 0:
        steps = ["book appointment"]

    return {
        "plan": steps[:3],
        "step": 0
    }