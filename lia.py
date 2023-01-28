import os
import json

class Interpreter:
    def __init__(self):
        self.commands = {}
        self.variables = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def register_variable(self, name, value):
        self.variables[name] = value

    def execute(self, program):
        for line in program.split("\n"):
            parts = line.split(" ")
            command = parts[0]
            args = parts[1:]
            if command in self.commands:
                if callable(self.commands[command]):
                    self.commands[command](*args)
                else:
                    os.system(self.commands[command])
            else:
                print(f"Unknown command: {command}")

    def run_lia_file(self, file):
        try:
            with open(file, "r") as f:
                program = f.read()
                self.execute(program)
        except FileNotFoundError:
            print(f"File {file} not found.")
    def save_commands(self):
        with open("commands.json", "w") as f:
            json.dump(self.commands, f)
    def load_commands(self):
        try:
            with open("commands.json", "r") as f:
                self.commands = json.load(f)
        except FileNotFoundError:
            print("No saved commands found.")

def add_command(interpreter, command_name, command_func):
    interpreter.register_command(command_name, command_func)
    print(f"Command {command_name} has been added.")

def remove_command(interpreter, command_name):
    if command_name in interpreter.commands:
        interpreter.commands.pop(command_name)
        print(f"Command {command_name} has been removed.")
    else:
        print(f"Command {command_name} not found.")

def add_variable(interpreter, variable_name, variable_value):
    interpreter.register_variable(variable_name, variable_value)
    print(f"Variable {variable_name} has been added with value {variable_value}.")

def remove_variable(interpreter, variable_name):
    if variable_name in interpreter.variables:
        interpreter.variables.pop(variable_name)
        print(f"Variable {variable_name} has been removed.")
    else:
        print(f"Variable {variable_name} not found.")

def run_terminal_command(interpreter, command):
    os.system(command)

interpreter = Interpreter()
interpreter.load_commands()

print("Welcome to the LIA programming language customizer.")
while True:
    print("Please choose from the following options:")
    print("1. Add a new command")
    print("2. Remove a command")
    print("3. Add a new variable")
    print("4. Remove a variable")
    print("5. Run a .lia file")
    print("6. Save commands")
    print("7. Exit the program.")
    choice = input("Enter your choice: ")

    if choice == "1":
        command_name = input("Enter the name of the command: ")
        command_func = input("Enter the command function: ")
        add_command(interpreter, command_name, command_func)
    elif choice == "2":
        command_name = input("Enter the name of the command: ")
        remove_command(interpreter, command_name)
    elif choice == "3":
        variable_name = input("Enter the name of the variable: ")
        variable_value = input("Enter the value of the variable: ")
        add_variable(interpreter, variable_name, variable_value)
    elif choice == "4":
        variable_name = input("Enter the name of the variable: ")
        remove_variable(interpreter, variable_name)
    elif choice == "5":
        file_name = input("Enter the name of the .lia file: ")
        interpreter.run_lia_file(file_name)
    elif choice == "6":
        interpreter.save_commands()
    elif choice == "7":
        break
    else:
        print("Invalid choice.")

    print("Exiting the program.")

