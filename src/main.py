import os
from classes import recorder, listener, bot
from functions import functions as f

API_TOKEN = "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"

def talk_and_response(r: recorder.Recorder, l: listener.Listener) -> str:
    os.system(f.command())
    
    print("Grabando...")
    print("Pulsa 'control + c' para parar")
    r.rec()
    r.exportFile()
    
    print("Transcribiendo...")
    answer = l.listen_audio()
    
    print("\nAnswer:\n", answer)
    
    res = bot.Bot(API_TOKEN, answer)
    response = res.respond()
    
    answer = ""
    
    return response

def main():
    r = recorder.Recorder()
    l = listener.Listener()
    
    os.system(f.command())
    init = True
    
    print("//"+"-"*15 + "Welcome to ChatGPT 3.0 :D" + "-"*15+"//")
    
    while(init):
        option = f.menu()
        
        if option == 1:
            response = talk_and_response(r, l)    
            print("\nResponse:", response)
            input("\nPress 'Enter' to continue\n")
        
        elif option == 2:
            init = False
        
        else:
            print("Opción incorrecta\n")
            os.system(f.command())
    
    return 0
    
if __name__ == "__main__":
    main()