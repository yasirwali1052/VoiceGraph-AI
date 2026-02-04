from langgraph.graph import StateGraph, END
from state import AgentState
from nodes.listen import listen_node
from nodes.plan import plan_node
from nodes.search import search_node
from nodes.create_doc import create_doc_node
from nodes.speak import speak_node

def create_workflow():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("listen", listen_node)
    workflow.add_node("plan", plan_node)
    workflow.add_node("search", search_node)
    workflow.add_node("create_doc", create_doc_node)
    
    workflow.set_entry_point("listen")
    
    workflow.add_edge("listen", "plan")
    workflow.add_edge("plan", "search")
    workflow.add_edge("search", "create_doc")
    workflow.add_edge("create_doc", END)
    
    return workflow.compile()