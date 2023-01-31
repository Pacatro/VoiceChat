import os
from functions import functions as f

def main():
    os.system(f.command())
    init = True
    
    print("//"+"-"*15 + "Welcome to ChatGPT 3.0 :D" + "-"*15+"//")
    
    while(init):
        option = f.menu()
        
        if option == 1:
            response = f.listen_and_response()    
            print("\nResponse:", response)
            input("\nPress 'Enter' to continue\n")
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