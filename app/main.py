import sys


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
            case _:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
