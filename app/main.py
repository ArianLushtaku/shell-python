import sys

commands = {
    "echo": lambda *x: print(" ".join(x)),
    "exit": lambda x=None: exit()
}

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
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

if __name__ == "__main__":
    main()
