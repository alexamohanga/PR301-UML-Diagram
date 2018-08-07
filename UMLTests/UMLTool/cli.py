import sys
import pylint.pyreverse

command_list = []
help_list = [
    ["help", "This command shows the help text. Like this"],
    ["open", "Opens a Python File and parses "],
    ["output", "Syntax: output <type> <output_file>" +
     "\n\t\t   Generates diagram from the specified type\n\t\t    and saves it to the <output_file> location"],
    ["exit", "Exits the application\"s shell."]
]

#pyreverse.main.Run()


class CLI:
    exit_requested = False

    def __init__(self):
        # Auto fill the command list from the help list
        for command in help_list:
            command_list.append(command[0])

        # Welcome messages
        print("\nWelcome to the Python 3 UML CLI Shell!")
        print("\tShell by Brandon De Rose\n")
        print("Tip: Type 'help' for a list of commands\n\n")

    def check_commandline(self):
        command = ""
        if len(sys.argv) > 1:
            command = sys.argv[1]
        args = []
        if len(sys.argv) > 2:
            args = sys.argv[2:]

        if command not in command_list:
            return False
        self.run_command(command, args)
        return True

    def check_input(self):
        # Get command input from stdin
        command = input("UMLCli# ")
        # Execute the command using method
        argv = command.split(" ")

        self.run_command(argv[0], argv[1:])
        # If exit is not requested then recursively check input again
        if not self.exit_requested:
            self.check_input()

    def run_command(self, command, args=[]):
        if command == "":
            return
        if command not in command_list:
            print("Command not found. Try using the 'help' command.")
            self.check_input()
            return
        getattr(self, command)(args)

    @staticmethod
    def help(args=[]):
        print("\nList of available commands:")
        for help_item in help_list:
            print("\t" + help_item[0] + "\t=> " + help_item[1])
        # New line
        print("")

    def exit(self, args=[]):
        self.exit_requested = True
        print("Bye!\n")


theCli = CLI()
if not theCli.check_commandline():
    theCli.check_input()

