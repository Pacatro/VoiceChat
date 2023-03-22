import platform
from classes import recorder, listener, bot

def menu() -> int:
    print("\n1. Talk")
    print("2. Exit\n")
    
    option = int(input("Option: "))
    
    return option

def command():
    system_os = platform.system()
    if system_os == "Linux":
        return "clear"

    return "cls"

def listen_and_response() -> str:
    r = recorder.Recorder()
    l = listener.Listener()
    
    print("Grabando...")
    print("Pulsa 'control + c' para parar")
    r.rec()
    
    transcription = l.transcribe_audio()
    
    return transcription

def bot_response(b: bot.Bot, prompt: str):
    b.set_prompt(prompt)
    b.response()