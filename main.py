import sys

def main():
    # List to store commands
    commands_list = ['exit', 'echo']
    # List to store arguments
    arguments_list = ['0']
    # Exit status
    exit_status = 0
    
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input and split it into a list of command and command's arguments
        user_input = input().strip().split()
        # If the inputed command is not in the list of commands
        if user_input[0] not in commands_list:
            print(f'{user_input[0]}: command not found')
        else:
            if user_input[0] == commands_list[0]:  # If the inputed command is exit
                if len(user_input) > 1:  # If the inputed exit command was with arguments
                      if user_input[1] == arguments_list[0]:  # If the inputed arguments is 0
                            exit_status = 0
                            return sys.exit(exit_status)
                else:  # If the inputed exit command was without arguments
                    argument = input()  # Wait for argument input
                    if argument == arguments_list[0]:  # If the inputed argument is 0
                        exit_status = 0
                        return sys.exit(exit_status)
            elif user_input[0] == commands_list[1]:  # If the inputed command is echo
                if len(user_input) > 1:  # If the inputed echo command was with arguments
                    print(' '.join(user_input[1:]))  # Echo the arguments
                else:  # If the inputed echo command was without arguments
                    argument = input()  # Wait for argument input
                    print(argument)        

if __name__ == "__main__":
    main()
