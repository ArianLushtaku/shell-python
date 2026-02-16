import sys

commands = {
    "echo": print("Hello")
}


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        pass

        command = input()
        match command:
            case "exit":
                return False
            case command if "echo" in command:
                print(f"{command.replace("echo ", "")}")
            case command if command in commands:
                return commands[command]

if __name__ == "__main__":
    main()
