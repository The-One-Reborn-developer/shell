import sys

def main():
    # List to store commands
    commands_list = ['exit']
    # List to store arguments
    arguments_list = ['0']
    # Exit status
    exit_status = 0
    
    while True:
        # Print the standard shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input and split it into a list of command and command's arguments
        user_input = input().split()
        
        # If the inputed command is not in the list of commands
        if user_input[0] not in commands_list:
            print(f'{user_input[0]}: command not found')
        else:
            if user_input[0] == commands_list[0]:  # If the inputed command is exit
                if len(user_input) > 1:  # If the inputed exit command was with arguments
                      if user_input[1] == arguments_list[0]:  # If the inputed arguments is 0
                            exit_status = 0
                            break
                else:  # If the inputed exit command was without arguments
                    argument = input()  # Wait for argument input
                    if argument == arguments_list[0]:  # If the inputed argument is 0
                        exit_status = 0
                        break
        
    return sys.exit(exit_status)

if __name__ == "__main__":
    main()
