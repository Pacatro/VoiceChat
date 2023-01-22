import platform

def menu() -> int:
    print("//"+"-"*15 + "Welcome to ChatGPT 3.0 :D" + "-"*15+"//")
    
    print("\n1. Talk to ChatGPT")
    print("2. Exit")
    
    option = int(input("Option: "))
    
    return option

def command():
    system_os = platform.system()
    if system_os == 'Linux':
        return "clear"

    return "cls"
