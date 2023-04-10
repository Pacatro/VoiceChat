import os
from functions import functions as f
from classes.bot import Bot
from sys import argv

def main():
    if len(argv) != 2:
        print("You need to have an OpenAI API key")
        print("Use example: python3 main.py <api_key>")
        return 0
    
    api_key = argv[1]
    
    b = Bot(api_key)
    os.system(f.command())
    init = True
    
    print("//"+"-"*15 + "Asistente de voz" + "-"*15+"//")
    
    while(init):
        option = f.menu()
        
        if option == 1:
            print("\n")
            answer = f.listen_and_response()    
            print("\nTú:", answer, "\n")
            f.bot_response(b, answer)
        
        elif option == 2:
            os.system(f.command())
            init = False
        
        else:
            print("Opción incorrecta\n")
            input("Pulsa 'Enter' para continuar\n")
            os.system(f.command())
    
    return 0
    
if __name__ == "__main__":
    main()