import platform
import os
from classes import recorder, listener, bot

def menu() -> int:
    print("\n1. Talk")
    print("2. Exit\n")
    
    option = int(input("Option: "))
    
    return option

def command():
    system_os = platform.system()
    if system_os == 'Linux':
        return "clear"

    return "cls"

def listen_and_response() -> str:
    os.system(command())
    
    r = recorder.Recorder()
    l = listener.Listener()
    
    print("Grabando...")
    print("Pulsa 'control + c' para parar")
    r.rec()
    
    print("Transcribiendo...")
    transcription = l.transcribe_audio()
    
    return transcription

def bot_response(prompt: str):
    b = bot.Bot(prompt)
    b.response()