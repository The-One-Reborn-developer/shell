import sys
import os
import subprocess

def main():
    commands_list = ['exit', 'echo', 'type', 'pwd', 'cd']  # List to store commands
    arguments_list = ['0', '~']  # List to store arguments
    exit_status = 0  # Exit status
    
    while True:
        sys.stdout.write("$ ")  # Write a standart shell prompt to stdout
        sys.stdout.flush()

        # Wait for user input and split it into a list of command and command's arguments
        user_input = input().strip().split()

        if not user_input:  # If the user didn't input anything
            continue

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
        elif user_input[0] == commands_list[2]:  # If the inputed command is type
            if len(user_input) > 1:  # If the inputed type command was with arguments
                if user_input[1] in commands_list:  # If the inputed argument is a command
                    print(f'{user_input[1]} is a shell builtin')
                elif user_input[1] not in commands_list:
                    find_command_result = find_command(user_input[1])
                    if find_command_result:
                        print(f'{user_input[1]} is {find_command_result}')
                    else:
                        print(f'{user_input[1]}: not found')
        elif user_input[0] == commands_list[3]:  # If the inputed command is pwd
            print(os.getcwd())
        elif user_input[0] == commands_list[4]:  # If the inputed command is cd
            try:
                if len(user_input) > 1:  # If the inputed cd command was with arguments
                    if user_input[1] == arguments_list[1]:  # Go to home directory
                        os.chdir(os.path.expanduser(arguments_list[1]))
                    else:
                        os.chdir(user_input[1])
                else:  # If the inputed cd command was without arguments
                    argument = input()  # Wait for argument input
                    os.chdir(argument)
            except FileNotFoundError:
                print(f'{user_input[0]}: {user_input[1]}: No such file or directory')
        elif find_command(user_input[0]):  # If the input is a program that is in PATH
            execute_program(user_input[0], user_input[1:])
        else:
            print(f'{user_input[0]}: command not found')


def find_command(command):
    '''
    Function to find a command that is in PATH

    Parameters
    ----------
    command : str
        The name of the command

    Returns
    -------
    str
        The path of the command
    '''
    path_dirs = os.environ.get('PATH', '').split(os.pathsep)
    for directory in path_dirs:  # Check each directory in PATH
        for root, dirs, files in os.walk(directory):  # Check each subdirectory in the directory
            for name in files:  # Check each file in the directory
                if name == command:
                    return os.path.abspath(os.path.join(root, name))
    
    return None


def execute_program(program, arguments):
    '''
    Function to execute a program

    Parameters
    ----------
    program : str
        The name of the program
    arguments : list
        The arguments to pass to the program

    Returns
    -------
    None
    '''
    program_path = find_command(program)  # Find the path of the program
    if program_path:
        try:
            result = subprocess.run([program_path] + arguments)
        except Exception as RunError:
            print(f'Error executing {program}: {RunError}')
    else:
        print(f'{program}: command not found')


if __name__ == "__main__":
    main()

