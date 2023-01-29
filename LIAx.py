import os,json
class I:
    def __init__(self):self.c=json.load(open("lia_commands.json")) if os.path.isfile("lia_commands.json") else {}
    def r(self,n,c):self.c[n]=c
    def e(self,p):
        for l in p.split("\n"):
            c,*a=l.split(" ");f=self.c.get(c);(callable(f)and f(*a) or os.system(f))if f else print(f"Unknown command: {c}")
    def rf(self,f):self.e(open(f).read())if os.path.isfile(f) else print(f"File {f} not found.")
    def l(self):[print(c) for c in self.c]
    def s(self):json.dump(self.c,open("lia_commands.json","w"))
    def rc(self,n):
        f=self.c.get(n)
        (callable(f)and f() or os.system(f))if f else print(f"Unknown command: {n}")
    def dirl(self):[print(f) for f in os.listdir() if f.endswith(".lia")]
    def create_file(self): os.system("nano new_file.lia")

i=I();a="\033[91;1m"+"""
 
 ██████╗ ██████╗ ███╗   ██╗███████╗ ██████╗ ██╗     ██████╗ 
██╔════╝██╔═████╗████╗  ██║██╔════╝██╔═████╗██║     ╚════██╗
██║     ██║██╔██║██╔██╗ ██║███████╗██║██╔██║██║      █████╔╝
██║     ████╔╝██║██║╚██╗██║╚════██║████╔╝██║██║      ╚═══██╗
╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═════╝ 
 
╦  ╦╔═╗
║  ║╠═╣    
╩═╝╩╩ ╩
┌─┐┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐┌┬┐┬┌┐┌┌─┐  ┬  ┌─┐┌┐┌┌─┐┬ ┬┌─┐┌─┐┌─┐
├─┘├┬┘│ ││ ┬├┬┘├─┤│││││││││││ ┬  │  ├─┤││││ ┬│ │├─┤│ ┬├┤ 
┴  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴┴ ┴┴┘└┘└─┘  ┴─┘┴ ┴┘└┘└─┘└─┘┴ ┴└─┘└─┘                                                             
"""+"\033[0m";print(a);print("Welcome to the LIA programming language customizer.")
while True:
    print("Please choose from the following options:")
    print("1. Add a new command")
    print("2. Run a .lia file")
    print("3. List all registered commands")
    print("4. Save commands to a file")
    print("5. Run specific command")
    print("6. List all .lia files in directory")
    print("7. Create a new .lia file")
    print("8. Exit the program.")
    choice = input("Enter your choice: ")

    if choice == "1":
        command_name = input("Enter the name of the command: ")
        command_func = input("Enter the command function: ")
        i.r(command_name, command_func)
    elif choice == "2":
        file_name = input("Enter the name of the .lia file: ")
        i.rf(file_name)
    elif choice == "3":
        i.l()
    elif choice == "4":
        i.s()
    elif choice == "5":
        command_name = input("Enter the name of the command to run: ")
        i.rc(command_name)
    elif choice == "6":
        i.dirl()
    elif choice == "7":
        i.create_file()
    elif choice == "8":
        break
    else:
        print("Invalid choice.")
print("Exiting the program.")
