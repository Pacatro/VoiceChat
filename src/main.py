import os
from functions import functions as f

def main():
    os.system(f.command())
    init = True
    
    print("//"+"-"*15 + "Welcome to a try of made Jarvis :D" + "-"*15+"//")
    
    while(init):
        option = f.menu()
        
        if option == 1:
            answer = f.listen_and_response()    
            print("\nRespuesta:", answer)
            f.bot_response(answer)
            input("\nPulsa 'Enter' para continuar\n")
            os.system(f.command())
        
        elif option == 2:
            os.system(f.command())
            init = False
        
        else:
            print("Opción incorrecta\n")
            os.system(f.command())
    
    return 0
    
if __name__ == "__main__":
    main()