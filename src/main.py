import os
from functions.functions import listen_and_response, menu, command, bot_response
from classes.bot import Bot
from sys import argv

def main():
    if len(argv) != 2:
        print("You need to have an OpenAI API key")
        print("Use example: python3 main.py <api_key>")
        return 0
    
    api_key = argv[1]
    
    b = Bot(api_key)
    os.system(command())
    init = True
    
    print("//"+"-"*15 + "VoiceChat" + "-"*15+"//")
    
    while(init):
        option = menu()
        
        if option == 1:
            print("\n")
            answer = listen_and_response()    
            print("\nYou:", answer, "\n")
            bot_response(b, answer)
        
        elif option == 2:
            os.system(command())
            init = False
        
        else:
            print("Incorrect option\n")
            input("Press 'Enter' to continue\n")
            os.system(command())
    
    return 0
    
if __name__ == "__main__":
    main()