from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    user_request: str
    plan: str
    search_results: List[dict]
    analysis: str
    document_path: str
    user_approval: bool
    messages: List[str]