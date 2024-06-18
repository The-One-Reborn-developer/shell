import sys

def main():
    # Print standard shell prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # List to store commands
    commands_list = []
    # Read user input
    user_input = input()

    # If the command that user has inputed is not in the list of commands
    if user_input not in commands_list:
        print(f'{user_input}: command not found')    

if __name__ == "__main__":
    main()
