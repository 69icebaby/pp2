#Ex.1
import os

def list_directories_and_files(path):
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        print("Directories:", directories)

        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        print("Files:", files)

        all_items = os.listdir(path)
        print("All Directories and Files:", all_items)

    except FileNotFoundError:
        print("Specified path not found.")

path = "/your/specified/path"
list_directories_and_files(path)

#Ex.2
import os

def check_path_access(path):
    try:
        exists = os.path.exists(path)
        readable = os.access(path, os.R_OK)
        writable = os.access(path, os.W_OK)
        executable = os.access(path, os.X_OK)

        print("Exists:", exists)
        print("Readable:", readable)
        print("Writable:", writable)
        print("Executable:", executable)

    except FileNotFoundError:
        print("Specified path not found.")

path = "/your/specified/path"
check_path_access(path)


#Ex.3

import os

def test_path_existence(path):
    try:
        exists = os.path.exists(path)
        print("Path exists:", exists)

        if exists:
            filename = os.path.basename(path)
            directory = os.path.dirname(path)

            print("Filename:", filename)
            print("Directory:", directory)

    except FileNotFoundError:
        print("Specified path not found.")

path = "/your/specified/path/file.txt"
test_path_existence(path)


#Ex.4

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print("Number of lines in the file:", len(lines))

    except FileNotFoundError:
        print("File not found.")

file_path = "/your/specified/path/file.txt"
count_lines_in_file(file_path)

#Ex.5

def write_list_to_file():
    try:
        input_list = input("Enter elements of the list (comma-separated): ").split(',')

        file_path = input("Enter the file path: ")

        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(str(item) + "\n")

        print("List written to the file successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

write_list_to_file()


#Ex.6

import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_path = f"{letter}.txt"
        with open(file_path, 'w') as file:
            file.write(f"Contents of {letter}.txt")

generate_text_files()

#Ex.7

def copy_file_contents():
    try:
        source_path = input("Enter the source file path: ")

        destination_path = input("Enter the destination file path: ")

        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)

        print("Contents copied successfully.")

    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_file_contents()

#Ex.8

import os

def delete_file_by_path():
    try:
        file_path = input("Enter the file path to be deleted: ")

        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} deleted successfully.")
        else:
            print(f"{file_path} not found.")

    except PermissionError:
        print(f"Permission error. Unable to delete {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

delete_file_by_path()


