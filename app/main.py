import sys
import os
import shutil
import subprocess

commands = {
    "echo": lambda *x: print(" ".join(x)),
    "exit": lambda x=None: exit(),
    "type": lambda *x: print(f"{x[0]} is a shell builtin") if x[0] in commands else pathType(x),
    "pwd": lambda x=None: print(f'{os.getcwd()}') if not x else print(f"pwd: too many arguments"),
    "cd": lambda x: changeDirectory(x) if x == ".." or os.access(x, os.F_OK) else print(f"cd: no such file or directory: {x}")
}

def pathType(x):
    x = x[0]
    if path := shutil.which(x):
        print(f"{x} is {path}")
    else:
        print(f'{x}: not found')
    
def changeDirectory(x): 
    path = os.getcwd()
    naked_path = path.split(os.path.sep)
    if x == "..":
        path = "/".join(naked_path[:-1])
        os.chdir(path)
    elif x in os.listdir(path):
        os.chdir("/".join(naked_path + x.split(os.path.sep)))
    else:
        os.chdir(x)

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
                args = args or ()
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
