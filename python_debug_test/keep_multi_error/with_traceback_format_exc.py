import traceback

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        # 使用 format_exc() 获取异常信息并打印
        error_message = traceback.format_exc()
        print(f"Error occurred in division:\n{error_message}")

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError as e:
        # 使用 format_exc() 获取异常信息并打印
        error_message = traceback.format_exc()
        print(f"Error occurred in access_list_element:\n{error_message}")

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        # 使用 format_exc() 获取异常信息并打印
        error_message = traceback.format_exc()
        print(f"Error occurred in open_file:\n{error_message}")

def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        # 使用 format_exc() 获取异常信息并打印
        error_message = traceback.format_exc()
        print(f"Error occurred in convert_to_int:\n{error_message}")

def call_nonexistent_method():
    try:
        obj = None
        obj.some_method()
    except AttributeError as e:
        # 使用 format_exc() 获取异常信息并打印
        error_message = traceback.format_exc()
        print(f"Error occurred in call_nonexistent_method:\n{error_message}")

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
        # 使用 format_exc() 获取异常信息并打印
        error_message = traceback.format_exc()
        print(f"An unexpected error occurred:\n{error_message}")
