from typing import TypedDict, List

class AgentState(TypedDict):
    input: str
    plan: List[str]
    step: int
    result: str
    max_steps: int 
    