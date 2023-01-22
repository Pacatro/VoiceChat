import os
from chatgpt_wrapper import ChatGPT
from classes import recorder, listener
from functions import functions as f

def talk_and_response(r: recorder.Recorder, l: listener.Listener) -> str:
    os.system(f.command())
    
    print("Grabando...")
    print("Pulsa 'control + c' para parar")
    r.rec()
    r.exportFile()
    
    print("Transcribiendo...")
    answer = l.listen_audio()
    
    return answer

def main():
    r = recorder.Recorder()
    l = listener.Listener()
    bot = ChatGPT()
    
    os.system(f.command())
    init = True
    
    while(init):
        option = f.menu()
        
        if option == 1:
            answer = talk_and_response(r, l)
            print("\nAnswer:\n", answer)

            response = bot.ask(answer)
            print("\nResponse:\n", response)
            input("\nPresiona 'enter' para continuar\n")
        elif option == 2:
            init = False
        else:
            print("Opción incorrecta\n")
            os.system(f.command())
    
    return 0
    
if __name__ == "__main__":
    main()