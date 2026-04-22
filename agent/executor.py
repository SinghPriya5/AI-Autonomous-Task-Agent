from utils.llm import call_llm
from agent.tools import book_appointment, set_reminder

def executor(state):
    step = state["step"]
    plan = state["plan"]
    user_input = state["input"]
    history = state.get("history", [])

    if step >= len(plan):
        return {
            "result": "\n".join(history),
            "step": step,
            "history": history
        }

    current_step = plan[step].lower()

    # 🔥 Extract person + date dynamically
    extract_prompt = f"""
    Extract details from this:

    Input: {user_input}

    Return JSON:
    {{
        "person": "...",
        "date": "..."
    }}
    """

    details = call_llm(extract_prompt)

    # simple parsing (for now)
    person = "the person"
    date = "tomorrow"

    if "teacher" in user_input.lower():
        person = "Teacher"
    elif "doctor" in user_input.lower():
        person = "Dr. Sharma"

    # EXECUTION
    if "book" in current_step:
        result = book_appointment(person, date)

    elif "remind" in current_step:
        result = set_reminder("Visit", "9 AM")

    else:
        result = "⚠️ Step skipped"

    history.append(result)

    return {
        "step": step + 1,
        "history": history,
        "result": result
    }