import speech_recognition as sr
from state import AgentState

def listen_node(state: AgentState) -> AgentState:
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 0.8
    
    with sr.Microphone() as source:
        print("Adjusting for background noise... Wait 2 seconds")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Speak NOW clearly!")
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except:
        text = input("Couldn't hear. Type: ")
    
    state["user_request"] = text
    state["messages"] = [f"User: {text}"]
    return state