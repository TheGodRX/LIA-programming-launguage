import os
import json

class Interpreter:
    def __init__(self):
        self.commands = {}
        try:
            with open("lia_commands.json", "r") as f:
                self.commands = json.load(f)
        except FileNotFoundError:
            pass
    
    def register_command(self, name, command):
        self.commands[name] = command
    
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
    def list_commands(self):
        for command in self.commands:
            print(command)
    def save_commands(self):
        with open("lia_commands.json", "w") as f:
            json.dump(self.commands, f)
    def run_specific_command(self, command_name):
        if command_name in self.commands:
            command = self.commands[command_name]
            if callable(command):
                command()
            else:
                os.system(command)
        else:
            print(f"Unknown command: {command_name}")

interpreter = Interpreter()
ascii_art = "\033[91;1m" + """
 
 ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗     ██████╗ 
██╔════╝██╔═████╗████╗  ██║██╔════╝██╔═████╗██║     ╚════██╗
██║     ██║██╔██║██╔██╗ ██║███████╗██║██╔██║██║      █████╔╝
██║     ████╔╝██║██║╚██╗██║╚════██║████╔╝██║██║      ╚═══██╗
╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═════╝ 
                                                            
""" + "\033[0m"

print(ascii_art)

# rest of the script
print("Welcome to the LIA programming language customizer.")
while True:
    print("Please choose from the following options:")
    print("1. Add a new command")
    print("2. Run a .lia file")
    print("3. List all registered commands")
    print("4. Save commands to a file")
    print("5. Run specific command")
    print("6. Exit the program.")
    choice = input("Enter your choice: ")

    if choice == "1":
        command_name = input("Enter the name of the command: ")
        command_func = input("Enter the command function: ")
        interpreter.register_command(command_name, command_func)
    elif choice == "2":
        file_name = input("Enter the name of the .lia file: ")
        interpreter.run_lia_file(file_name)
    elif choice == "3":
        interpreter.list_commands()
    elif choice == "4":
        interpreter.save_commands()
    elif choice == "5":
        command_name = input("Enter the name of the command to run: ")
        interpreter.run_specific_command(command_name)
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
print("Exiting the program.")

