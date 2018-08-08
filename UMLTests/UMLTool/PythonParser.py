import os.path

class PythonStatement:
    def __init__(self, line):
        self.items = line.strip().split()
        self.indention = len(line) - len(line.lstrip())
        print("Item: " + self.items[0] + " Indentation: " + str(self.indention))

    def is_class(self):
        return self.items[0] == "class"

    def is_def(self):
        return self.items[0] == "def"

    def get_name(self):
        if len(self.items) > 1:
            return self.items[1]
        return "None"

class PythonClass:
    def __init__(self, name, indention, statements_in_scope=[]):
        self.name = name
        self.indention = indention
        self.statements = statements_in_scope
        print("Class parsed: " + self.name)

    def add_statement(self, new_statement):
        self.statements.append(new_statement)

class PythonParser:
    def __init__(self):
        self.class_list = []
        self.file_lines = []
        self.statements = []
        pass

    def input(self, file_path):
        print("Validating: " + file_path)
        if not self.validate_python_file(file_path):
            print("Failed to validate input file: " + file_path)
            return

        print("Successfully Validated: " + file_path)
        self.parse(file_path)

    def validate_python_file(self, file_path):
        if not os.path.isfile(file_path):
            print("Error: File was not found: " + file_path)
            return False

        try:
            source = open(file_path, 'r').read() + '\n'
            compile(source, file_path, 'exec')
        except SyntaxError as e:
            print("Error: Failed to validate python code. Please provide valid Python code: \nPython Error: " + str(e))
            return False
        except SyntaxWarning as e:
            print("Warning: A syntax warning was found: \nPython Warning: " + str(e))
        except:
            print("Error: An unidentified error occurred")
            return False

        return True

    def parse(self, file_path):
        source = open(file_path, 'r').read() + '\n'

        self.file_lines += source.split("\n")
        original_count = len(self.file_lines)

        for line in self.file_lines:
            if line.strip() == "":
                self.file_lines.remove(line)
                continue
            self.statements.append(PythonStatement(line))

        print("Parsed " + str(original_count) + " lines")
        print("Removed " + str(original_count - len(self.file_lines)) + " empty lines")
        self.parse_classes()

    def parse_classes(self):
        current_class = None
        for statement in self.statements:
            if statement.is_class():
                if current_class is not None:
                    self.class_list.append(current_class)
                current_class = PythonClass(statement.get_name(), statement.indention)
            if current_class is not None:
                current_class.add_statement(statement)


myParser = PythonParser()
myParser.input("./test_data/valid_class.py")
myParser.input("./test_data/invalid_class.py")