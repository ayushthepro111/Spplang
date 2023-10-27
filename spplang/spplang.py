import gc

class Splus:
    def __init__(self):
        self.custom_vars = {}
        self.results = {}

    def write(self, arg):
        """Print the value of a variable (Usage: write <variable_name>)"""
        if arg in self.custom_vars:
            value = self.custom_vars[arg]
            if isinstance(value, dict):
                for key, val in value.items():
                    print(f"{key}: {val}")
            else:
                print(value)
        gc.collect()

    def variable(self, arg):
        """Define or retrieve custom variables (Usage: variable <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            value = parts[1].strip()
            if name in self.custom_vars:
                print(f"Variable '{name}' is '{self.custom_vars[name]}'")
            self.custom_vars[name] = value
            print(f"Variable '{name}' set to '{value}'")
        else:
            print("Invalid syntax. Usage: variable <name> = <value>")

    def integer(self, arg):
        """Define or retrieve custom integer variables (Usage: integer <name> = <value>)"""
        name, value = self._parse_var_assignment(arg)
        if value is not None:
            self.custom_vars[name] = int(value)
            print(f"Integer '{name}' set to '{value}'")
        else:
            if name in self.custom_vars:
                print(f"Integer '{name}' is '{self.custom_vars[name]}'")
            else:
                print(f"Integer '{name}' is not defined")

    def float(self, arg):
        """Define or retrieve custom float variables (Usage: float <name> = <value>)"""
        name, value = self._parse_var_assignment(arg)
        if value is not None:
            self.custom_vars[name] = float(value)
            print(f"Float '{name}' set to '{value}'")
        else:
            if name in self.custom_vars:
                print(f"Float '{name}' is '{self.custom_vars[name]}'")
            else:
                print(f"Float '{name}' is not defined")

    def complex(self, arg):
        """Define or retrieve custom complex variables (Usage: complex <name> = <real> <imag>)"""
        name, value = self._parse_var_assignment(arg)
        if value is not None:
            real, imag = map(float, value.split())
            self.custom_vars[name] = complex(real, imag)
            print(f"Complex '{name}' set to '({real}+{imag}j)'")
        else:
            if name in this.custom_vars:
                print(f"Complex '{name}' is '{self.custom_vars[name]}'")
            else:
                print(f"Complex '{name}' is not defined")

    def _parse_var_assignment(self, arg):
        args = arg.split('=')
        name = args[0].strip()
        value = args[1].strip() if len(args) > 1 else None
        return name, value

    def withdraw(self, arg):
        """Subtract two numbers (Usage: withdraw <name> = <a> <b>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name, values = parts
            a, b = map(float, values.split())
            self.custom_vars[name] = a - b
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: withdraw <name> = <a> <b>")
        gc.collect()

    def into(self, arg):
        """Multiply two numbers (Usage: into <name> = <a> <b>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name, values = parts
            a, b = map(float, values.split())
            self.custom_vars[name] = a * b
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: into <name> = <a> <b>")
        gc.collect()

    def onto(self, arg):
        """Divide two numbers (Usage: onto <name> = <a> <b>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name, values = parts
            a, b = map(float, values.split())
            if b == 0:
                print("Division by zero is not allowed")
            else:
                self.custom_vars[name] = a / b
                print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: onto <name> = <a> <b>")
        gc.collect()

    def dis_length(self, arg):
        """Calculate the length of a string (Usage: dis_length <name> = <string>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            string_value = parts[1].strip()
            self.custom_vars[name] = len(string_value)
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: dis_length <name> = <string>")
        gc.collect()

    def listf(self, arg):
        """Create a list from arguments (Usage: listf <name> = <arg1> [<arg2> ...])"""
        parts = arg.split('=')
        if len(parts) >= 2:
            name = parts[0].strip()
            args = parts[1].split()
            result = list(map(float, args))
            self.custom_vars[name] = result
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: listf <name> = <arg1> [<arg2> ...]")
        gc.collect()

    def tuplef(self, arg):
        """Create a tuple from arguments (Usage: tuplef <name> = <arg1> [<arg2> ...])"""
        parts = arg.split('=')
        if len(parts) >= 2:
            name = parts[0].strip()
            args = parts[1].split()
            result = tuple(map(float, args))
            self.custom_vars[name] = result
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: tuplef <name> = <arg1> [<arg2> ...]")
        gc.collect()

    def rangef(self, arg):
        """Create a list using the range function (Usage: rangef <name> = <start> <stop> [<step>])"""
        parts = arg.split('=')
        if len(parts) == 2:
            name, args = parts[0].strip(), parts[1].strip().split()
            if len(args) >= 2:
                start, stop = map(int, args[:2])
                step = int(args[2]) if len(args) > 2 else 1
                result = list(range(start, stop, step))
                self.custom_vars[name] = result
                print(f"Variable '{name}' set to {self.custom_vars[name]}")
            else:
                print("Invalid syntax. Usage: rangef <name> = <start> <stop> [<step>]")
        else:
            print("Invalid syntax. Usage: rangef <name> = <start> <stop> [<step>]")
        gc.collect()

    def setf(self, arg):
        """Create a set from arguments (Usage: setf <name> = <arg1> [<arg2> ...])"""
        parts = arg.split('=')
        if len(parts) >= 2:
            name = parts[0].strip()
            args = parts[1].split()
            result = set(map(float, args))
            self.custom_vars[name] = result
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: setf <name> = <arg1> [<arg2> ...]")
        gc.collect()

    def frozset(self, arg):
        """Create a frozenset from arguments (Usage: frozset <name> = <arg1> [<arg2> ...])"""
        parts = arg.split('=')
        if len(parts) >= 2:
            name = parts[0].strip()
            args = parts[1].split()
            result = frozenset(map(float, args))
            self.custom_vars[name] = result
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: frozset <name> = <arg1> [<arg2> ...]")
        gc.collect()

    def boolean(self, arg):
        """Store or retrieve boolean values (Usage: boolean <name> [= True|False])"""
        args = arg.split("=")
        name = args[0].strip()

        if len(args) > 1:
            value = args[1].strip().lower()
            if value == "true":
                self.custom_vars[name] = True
                print(f"Variable '{name}' set to True")
            elif value == "false":
                self.custom_vars[name] = False
                print(f"Variable '{name}' set to False")
            else:
                print("Invalid boolean value. Please use 'True' or 'False'.")
        else:
            if name in self.custom_vars:
                value = self.custom_vars[name]
                print(f"Variable '{name}' is {value}")
            else:
                print(f"Variable '{name}' is not defined")

        gc.collect()

    def byte(self, arg):
        """Encode a string as bytes (Usage: byte <name> = <string>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            string_value = parts[1].strip()
            self.custom_vars[name] = string_value.encode()
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: byte <name> = <string>")
        gc.collect()

    def byte_arr(self, arg):
        """Create a byte array from a list of integers (Usage: byte_arr <name> = <int1> <int2> [<int3> ...])"""
        parts = arg.split('=')
        if len(parts) >= 2:
            name = parts[0].strip()
            args = parts[1].split()
            byte_array = bytearray(map(int, args))
            self.custom_vars[name] = byte_array
            print(f"Variable '{name}' set to {self.custom_vars[name]}")
        else:
            print("Invalid syntax. Usage: byte_arr <name> = <int1> <int2> [<int3> ...]")
        gc.collect()

    def help(self, arg):
        """Display help message for a command (Usage: help [command])"""
        if arg:
            command = arg.strip()
            if hasattr(self, command):
                docstring = getattr(self, command).__doc__
                if docstring:
                    print(docstring)
                else:
                    print(f"No help available for '{command}'")
            else:
                print(f"Unknown command '{command}'")
        else:
            available_commands = [method_name for method_name in dir(self) if callable(getattr(self, method_name))]
            print("Available commands:")
            for command in available_commands:
                docstring = getattr(self, command).__doc__
                if docstring:
                    print(f"{command}: {docstring}")
                else:
                    print(f"{command}: No help available")
        gc.collect()

    def exit(self, arg):
        """Exit the Splus interpreter (Usage: exit)"""
        print("Exiting Splus interpreter.")
        exit()

    def positive(self, arg):
        """Define or retrieve custom variables (Usage: positive <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            value = float(parts[1].strip())
            if name in self.custom_vars:
                self.custom_vars[name] = value
                print(f"Variable '{name}' set to {value}")
                return f"Variable '{name}' set to {value}"
            else:
                self.custom_vars[name] = value
                print(f"Variable '{name}' set to {value}")
                return f"Variable '{name}' set to {value}"
        else:
            print("Invalid syntax. Usage: positive <name> = <value>")
            return "Invalid syntax. Usage: positive <name> = <value>"

    def mini(self, arg):
        """Define or retrieve custom variables (Usage: mini <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            values = [float(val) for val in parts[1].strip().split()]
            minimum = min(values)
            if name in self.custom_vars:
                self.custom_vars[name] = minimum
                print(f"Variable '{name}' set to {minimum}")
                return f"Variable '{name}' set to {minimum}"
            else:
                self.custom_vars[name] = minimum
                print(f"Variable '{name}' set to {minimum}")
                return f"Variable '{name}' set to {minimum}"
        else:
            print("Invalid syntax. Usage: mini <name> = <value>")
            return "Invalid syntax. Usage: mini <name> = <value>"

    def maxi(self, arg):
        """Define or retrieve custom variables (Usage: maxi <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            values = [float(val) for val in parts[1].strip().split()]
            maximum = max(values)
            if name in self.custom_vars:
                self.custom_vars[name] = maximum
                print(f"Variable '{name}' set to {maximum}")
                return f"Variable '{name}' set to {maximum}"
            else:
                self.custom_vars[name] = maximum
                print(f"Variable '{name}' set to {maximum}")
                return f"Variable '{name}' set to {maximum}"
        else:
            print("Invalid syntax. Usage: maxi <name> = <value>")
            return "Invalid syntax. Usage: maxi <name> = <value>"

    def power(self, arg):
        """Define or retrieve custom variables (Usage: power <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            base, exponent = [float(val) for val in parts[1].strip().split()]
            result = 1
            for _ in range(int(exponent)):
                result *= base
            if name in self.custom_vars:
                self.custom_vars[name] = result
                print(f"Variable '{name}' set to {result}")
                return f"Variable '{name}' set to {result}"
            else:
                self.custom_vars[name] = result
                print(f"Variable '{name}' set to {result}")
                return f"Variable '{name}' set to {result}"
        else:
            print("Invalid syntax. Usage: power <name> = <base> <exponent>")
            return "Invalid syntax. Usage: power <name> = <base> <exponent>"

    def sq_root(self, arg):
        """Define or retrieve custom variables (Usage: sq_root <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            value = float(parts[1].strip())
            if value < 0:
                raise ValueError("Square root is not defined for negative numbers")
            guess = value / 2.0
            epsilon = 1e-6
            while abs(guess * guess - value) > epsilon:
                guess = (guess + value / guess) / 2.0
            if name in self.custom_vars:
                self.custom_vars[name] = guess
                print(f"Variable '{name}' set to {guess}")
                return f"Variable '{name}' set to {guess}"
            else:
                self.custom_vars[name] = guess
                print(f"Variable '{name}' set to {guess}")
                return f"Variable '{name}' set to {guess}"
        else:
            print("Invalid syntax. Usage: sq_root <name> = <value>")
            return "Invalid syntax. Usage: sq_root <name> = <value>"

    def cb_root(self, arg):
        """Define or retrieve custom variables (Usage: cb_root <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            value = float(parts[1].strip())
            if value < 0:
                raise ValueError("Cube root is not defined for negative numbers")
            guess = value / 2.0
            epsilon = 1e-6
            while abs(guess * guess * guess - value) > epsilon:
                guess = (2 * guess + value / (guess * guess)) / 3.0
            if name in self.custom_vars:
                self.custom_vars[name] = guess
                print(f"Variable '{name}' set to {guess}")
                return f"Variable '{name}' set to {guess}"
            else:
                self.custom_vars[name] = guess
                print(f"Variable '{name}' set to {guess}")
                return f"Variable '{name}' set to {guess}"
        else:
            print("Invalid syntax. Usage: cb_root <name> = <value>")
            return "Invalid syntax. Usage: cb_root <name> = <value>"

    def close(self, arg):
        """Define or retrieve custom variables (Usage: close <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            value = float(parts[1].strip())
            if value == int(value):
                result = int(value)
            elif value > 0:
                result = int(value) + 1
            else:
                result = int(value) - 1
            if name in self.custom_vars:
                self.custom_vars[name] = result
                print(f"Variable '{name}' set to {result}")
                return f"Variable '{name}' set to {result}"
            else:
                self.custom_vars[name] = result
                print(f"Variable '{name}' set to {result}")
                return f"Variable '{name}' set to {result}"
        else:
            print("Invalid syntax. Usage: close <name> = <value>")
            return "Invalid syntax. Usage: close <name> = <value>"

    def roundf(self, arg):
        """Define or retrieve custom variables (Usage: roundf <name> = <value>)"""
        parts = arg.split('=')
        if len(parts) == 2:
            name = parts[0].strip()
            value = float(parts[1].strip())
            if value == int(value):
                result = int(value)
            elif value > 0:
                result = int(value)
            else:
                result = int(value) - 1
            if name in self.custom_vars:
                self.custom_vars[name] = result
                print(f"Variable '{name}' set to {result}")
                return f"Variable '{name}' set to {result}"
            else:
                self.custom_vars[name] = result
                print(f"Variable '{name}' set to {result}")
                return f"Variable '{name}' set to {result}"
        else:
            print("Invalid syntax. Usage: roundf <name> = <value>")
            return "Invalid syntax. Usage: roundf <name> = <value>"

    def parse_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:  # Ignore empty lines
                    parts = line.split(" ", 1)
                    if len(parts) == 2:
                        cmd, arg = parts
                        if hasattr(self, cmd):
                            result = getattr(self, cmd)(arg)
                            self.results[cmd] = result
                        else:
                            self.results[cmd] = f"Unknown command '{cmd}'"
                    else:
                        self.results[cmd] = "Invalid command. Type 'help' for a list of commands."
        except FileNotFoundError:
            return "File not found"
        return self.results

if __name__ == '__main__':
    splus = Splus()
    while True:
        command = input("Enter a command: ").strip()
        if command:
            parts = command.split(" ", 1)
            if len(parts) == 2:
                cmd, arg = parts
                if hasattr(splus, cmd):
                    getattr(splus, cmd)(arg)
                else:
                    print(f"Unknown command '{cmd}'")
            else:
                print("Invalid command. Type 'help' for a list of commands.")
