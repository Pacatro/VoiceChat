import os
from functions import functions as f
from classes import bot

def main():
    b = bot.Bot()
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