import os
import shutil
import subprocess
import shlex
import sys
from typing import Callable, Any


#Directory of commands as keys and executeables as values.
commands: dict[str, Callable[..., Any]] = {
    "echo": lambda *x: " ".join(x),
    "exit": lambda *args: exit(),
    "type": lambda *x: None if len(x) < 1 else f"{x[0]} is a shell builtin" if x[0] in commands else pathType(x[0]),
    "pwd": lambda *args: f'{os.getcwd()}' if not args else f"pwd: too many arguments",
    "cd": lambda *args: changeDirectory("") if not args else changeDirectory(args[0])
}

#Type of command, when its not made by me, but is a system executeable command.
def pathType(x: str) -> str:
    if path := shutil.which(x):
        return f"{x} is {path}"
    else:
        return f'{x}: not found'

#Change directory command or cd.
def changeDirectory(x: str): 
    if x == "~" or x == "":
        home = os.getenv('HOME')
        if home:
            os.chdir(home)
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

def handleDirCommands(args: list[str], command: str, commands: dict[str, Callable[..., Any]]) -> Any:
    if ">" in args or "1>" in args:
        idx = args.index(">") if ">" in args else args.index("1>")
        f = open(args[idx + 1], "w")
        output = commands[command](*args[:idx])
        if output is not None:
            f.write(output)
            f.close()
    args = args or []
    return commands[command](*args)

def handleSystemCommands(parts: list[str], command: str) -> None:
    if ">" in parts or "1>" in parts:
        idx = parts.index(">") if ">" in parts else parts.index("1>")
        with open(parts[idx + 1], "w") as f:
            subprocess.call(parts[:idx], stdout=f)
    else:
        subprocess.call(parts)
        if command == "cat":
            pass

#Main code
def main():
    while True:
        try:
            sys.stdout.write("$ ")
            user_input = input()
            parts =  shlex.split(user_input)
            if parts == []:
                continue
            command = parts[0]
            args = parts[1:]

            #execute commands we defined
            if command in commands:
                result = handleDirCommands(args, command, commands)
                if result is not None:
                    print(result)
            #else if command is a system executeable, execute.
            elif (path := shutil.which(command)) and os.access(path, os.X_OK):
                handleSystemCommands(parts, command)

            else:
                print(f"{command}: command not found")

        #When pressing CTRL C, dont throw error, just close silently with Exiting..
        except KeyboardInterrupt:
            print("\nExiting...")
            break


    
if __name__ == "__main__":
    main()
