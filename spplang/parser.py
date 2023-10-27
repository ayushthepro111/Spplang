import spplang
from spplang import *

filename = input("Enter The File Name: ")
def parse_file(file_path):
    results = []  # Initialize an empty list to store results
    splus = Splus()  # Create an instance of the Splus class

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:  # Ignore empty lines
                parts = line.split(" ", 1)
                if len(parts) == 2:
                    cmd, arg = parts
                    if hasattr(splus, cmd):
                        result = getattr(splus, cmd)(arg)
                        if result is not None:  # Filter out None results
                            results.append(result)
                    else:
                        results.append(f"Unknown command '{cmd}'")
                else:
                    results.append("Invalid command. Type 'help' for a list of commands.")
    except FileNotFoundError as e:
        results.append(f"File not found: {str(e)}")
    except Exception as e:
        results.append(f"An error occurred: {str(e)}")
    return results

if __name__ == '__main__':
    file_path = filename
    results = parse_file(file_path)
    results = [result for result in results if result is not None]  # Filter out None results
    for result in results:
        print(result)
    while True:
    	user_input = input("Enter 'quit' to exit: ")
    	if user_input.lower() == 'quit':
            break
