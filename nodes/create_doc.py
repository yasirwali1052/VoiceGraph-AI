from state import AgentState
from tools.doc_creater import create_document
from langchain_groq import ChatGroq
from config import GROQ_API_KEY, GROQ_MODEL

llm = ChatGroq(api_key=GROQ_API_KEY, model=GROQ_MODEL, temperature=0)

def create_doc_node(state: AgentState) -> AgentState:
    search_results = state.get("search_results", [])
    user_request = state["user_request"]
    
    results_text = "\n".join([f"- {r['title']}: {r['body']}" for r in search_results[:3]])
    
    prompt = f"""Based on this request: {user_request}

And these search results:
{results_text}

Create a clear, concise summary document."""
    
    summary = llm.invoke(prompt).content
    state["analysis"] = summary
    
    doc_path = create_document(summary, "research_report.docx")
    state["document_path"] = doc_path
    
    return state