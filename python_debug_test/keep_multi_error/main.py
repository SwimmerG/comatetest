import traceback

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
        traceback.print_exc()

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        print(f"Error: Index {index} is out of bounds for the list.")
        traceback.print_exc()

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"Error: File {file_path} not found.")
        traceback.print_exc()

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        print(f"Error: Cannot convert {value} to integer.")
        traceback.print_exc()

def call_nonexistent_method():
    try:
        obj = None
        obj.some_method()
    except AttributeError as e:
        print("Error: Object has no attribute 'some_method'.")
        traceback.print_exc()

def execute_code():
    # Example executions
    division(10, 0)
    access_list_element([1, 2, 3], 5)
    open_file("non_existent_file.txt")
    convert_to_int("abc")
    call_nonexistent_method()

if __name__ == "__main__":
    try:
        execute_code()
    except Exception as e:
        print("An unexpected error occurred.")
        traceback.print_exc()
