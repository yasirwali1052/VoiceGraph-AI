from langchain_groq import ChatGroq
from config import GROQ_API_KEY, GROQ_MODEL
from state import AgentState

llm = ChatGroq(api_key=GROQ_API_KEY, model=GROQ_MODEL, temperature=0)

def plan_node(state: AgentState) -> AgentState:
    user_request = state["user_request"]
    
    prompt = f"""Create a brief plan for this task: {user_request}

Return only the plan as numbered steps, nothing else."""
    
    response = llm.invoke(prompt)
    state["plan"] = response.content
    
    return state