import sys
import os
import shutil

commands = {
    "echo": lambda *x: print(" ".join(x)),
    "exit": lambda x=None: exit(),
    "type": lambda *x: print(f"{"".join(x[0])} is a shell builtin") if x[0] in commands else pathType(x)
}

def pathType(x):
    if path := shutil.which(x[0]):
        print(f"{x[0]} is {path}")
    else:
        print(f'{x}: not found')

def main():
    PATH = "/usr/bin:/usr/local/bin:"
    while True:
        try:
            sys.stdout.write("$ ")
            pass

            user_input = input()
            parts =  user_input.split()
            command = parts[0]
            args = parts[1:]
            if command in commands:
                commands[command](*args)
            else:
                print(f"{command}: command not found")

        except KeyboardInterrupt as e:
            print("\nExiting!")
            break


    
if __name__ == "__main__":
    main()
