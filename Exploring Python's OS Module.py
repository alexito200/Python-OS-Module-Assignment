# Task 1: Directory Inspector

# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory.
# Handle exceptions for invalid paths or inaccessible directories.

import os

def list_directory_contents():
    user_path = input("Tell me what directory you would like the contents of (please provide a format of './directory_name' or '.' for the current working directory): ")
    
    try:
        contents = os.listdir(user_path)
        print("\nDirectory contents:", contents)
    except FileNotFoundError:
        print(f"\nError: The directory '{user_path}' does not exist.")
    except NotADirectoryError:
        print(f"\nError: '{user_path}' is not a directory.")
    except PermissionError:
        print(f"\nError: Permission denied to access '{user_path}'.")

list_directory_contents()
