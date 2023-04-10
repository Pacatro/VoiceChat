import platform
from classes.recorder import Recorder
from classes.listener import Listener
from classes.bot import Bot

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
    r = Recorder()
    l = Listener()
    
    print("Recording...")
    print("Press 'control+c' to stop")
    r.rec()
    
    transcription = l.transcribe_audio()
    
    return transcription

def bot_response(b: Bot, prompt: str):
    b.set_prompt(prompt)
    print("Writting...\n")
    b.response()