import platform
import os
from classes import recorder, listener, bot

API_TOKEN = "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"

def menu() -> int:
    print("\n1. Talk to ChatGPT")
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
    r.exportFile()
    
    print("Transcribiendo...")
    answer = l.listen_audio()
    
    print("\nAnswer:\n", answer)
    
    res = bot.Bot(API_TOKEN, answer)
    response = res.respond()
    
    return response