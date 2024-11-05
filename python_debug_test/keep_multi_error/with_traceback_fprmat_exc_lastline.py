import traceback

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        error_message = traceback.format_exc()
        # 只输出最后一行错误信息
        print(f"Error occurred in division:\n{error_message.splitlines()[-1]}")

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        error_message = traceback.format_exc()
        # 只输出最后一行错误信息
        print(f"Error occurred in access_list_element:\n{error_message.splitlines()[-1]}")

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        error_message = traceback.format_exc()
        # 只输出最后一行错误信息
        print(f"Error occurred in open_file:\n{error_message.splitlines()[-1]}")

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        error_message = traceback.format_exc()
        # 只输出最后一行错误信息
        print(f"Error occurred in convert_to_int:\n{error_message.splitlines()[-1]}")

def call_nonexistent_method():
    try:
        obj = None
        obj.some_method()
    except AttributeError as e:
        error_message = traceback.format_exc()
        # 只输出最后一行错误信息
        print(f"Error occurred in call_nonexistent_method:\n{error_message.splitlines()[-1]}")

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
        error_message = traceback.format_exc()
        # 只输出最后一行错误信息
        print(f"An unexpected error occurred:\n{error_message.splitlines()[-1]}")
