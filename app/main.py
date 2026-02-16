import sys
import os
import shutil
import subprocess

commands = {
    "echo": lambda *x: print(" ".join(x)),
    "exit": lambda x=None: exit(),
    "type": lambda *x: print(f"{"".join(x[0])} is a shell builtin") if x[0] in commands else pathType(x),
    "pwd": lambda x=None: print(f'{os.getcwd()}')
}

def pathType(x):
    x = x[0]
    if path := shutil.which(x):
        print(f"{x} is {path}")
    else:
        print(f'{x}: not found')

def main():
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
            elif (path := shutil.which(command)) and os.access(path, os.X_OK):
                subprocess.call(parts)
            else:
                print(f"{command}: command not found")

        except KeyboardInterrupt as e:
            print("\nExiting!")
            break


    
if __name__ == "__main__":
    main()
