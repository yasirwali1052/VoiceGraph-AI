from graph import create_workflow
from nodes.speak import speak

def main():
    app = create_workflow()
    
    speak("Hello! What would you like me to research?")
    
    initial_state = {
        "user_request": "",
        "plan": "",
        "search_results": [],
        "analysis": "",
        "document_path": "",
        "user_approval": True,
        "messages": []
    }
    
    result = app.invoke(initial_state)
    
    if result.get("document_path"):
        speak(f"Your document is ready at {result['document_path']}")
    else:
        speak("Could not complete the task.")

if __name__ == "__main__":
    main()