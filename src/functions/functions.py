import platform

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
