import traceback

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        # 输出错误类型
        error_type = type(e).__name__
        print(f"Error occurred in division: {error_type}")

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        # 输出错误类型
        error_type = type(e).__name__
        print(f"Error occurred in access_list_element: {error_type}")

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        # 输出错误类型
        error_type = type(e).__name__
        print(f"Error occurred in open_file: {error_type}")

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        # 输出错误类型
        error_type = type(e).__name__
        print(f"{error_type}")

def call_nonexistent_method():
    try:
        obj = None
        obj.some_method()
    except AttributeError as e:
        # 输出错误类型
        error_type = type(e).__name__
        print(f"{error_type}")

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
        # 输出错误类型
        error_type = type(e).__name__
        print(f"An unexpected error occurred: {error_type}")
