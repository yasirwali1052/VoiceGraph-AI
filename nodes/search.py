from state import AgentState
from tools.web_search import search_web
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, GROQ_MODEL

llm = ChatGroq(api_key=GROQ_API_KEY, model=GROQ_MODEL, temperature=0)

def search_node(state: AgentState) -> AgentState:
    user_request = state["user_request"]
    
    query_prompt = f"Create a search query for: {user_request}. Return only the query."
    query = llm.invoke(query_prompt).content.strip()
    
    results = search_web(query, max_results=5)
    state["search_results"] = results
    
    return state