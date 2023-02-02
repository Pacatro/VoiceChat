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
    answer = l.transcribe_audio()
    
    return answer

def bot_response(order: str):
    b = bot.Bot(order)
    b.open_orders()