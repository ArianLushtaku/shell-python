import sys
import os
import shutil
import subprocess
import shlex


#Directory of commands as keys and executeables as values.
commands = {
    "echo": lambda *x: print(" ".join(x)),
    "exit": lambda x=None: exit(),
    "type": lambda *x: print(f"{x[0]} is a shell builtin") if x[0] in commands else pathType(x),
    "pwd": lambda x=None: print(f'{os.getcwd()}') if not x else print(f"pwd: too many arguments"),
    "cd": lambda x=None: changeDirectory(x)
}

#Type of command, when its not made by me, but is a system executeable command.
def pathType(x):
    x = x[0]
    if path := shutil.which(x):
        print(f"{x} is {path}")
    else:
        print(f'{x}: not found')

#Change directory command or cd.
def changeDirectory(x): 
    if x == "~" or x is None:
        os.chdir(os.getenv('HOME'))
        return
    if os.access(x, os.F_OK):
        path = os.getcwd()
        naked_path = path.split(os.path.sep)
        if x in os.listdir(path):
            os.chdir("/".join(naked_path + x.split(os.path.sep)))
        else:
            os.chdir(x)
    else:
        print(f"cd: no such file or directory: {x}")

#Main code
def main():
    while True:
        try:
            sys.stdout.write("$ ")
            pass

            user_input = input()
            parts =  shlex.split(user_input)

            command = parts[0]
            args = parts[1:]
            #execute commands we defined
            if command in commands:
                args = args or ()
                commands[command](*args)
            #else if command is a system executeable, execute.
            elif (path := shutil.which(command)) and os.access(path, os.X_OK):
                subprocess.call(parts)
            else:
                print(f"{command}: command not found")

        #When pressing CTRL C, dont throw error, just close silently with Exiting..
        except KeyboardInterrupt as e:
            print("\nExiting...")
            break


    
if __name__ == "__main__":
    main()
