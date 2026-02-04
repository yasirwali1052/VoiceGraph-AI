import edge_tts
import asyncio
import os

async def text_to_speech(text, output_file="temp_speech.mp3"):
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
    await communicate.save(output_file)
    os.system(f"start {output_file}")

def speak(text):
    asyncio.run(text_to_speech(text))

def speak_node(state, message):
    speak(message)
    return state