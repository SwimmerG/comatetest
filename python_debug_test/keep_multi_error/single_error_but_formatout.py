import traceback

def calculate_average(numbers):
    try:
        total = sum(numbers)
        average = total / len(disk)  # 保留原始错误，将 disk 改为 numbers
        return average
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
        print(traceback.format_exc())  # 输出详细的 traceback 信息
    except TypeError as e:
        print("Error: Unsupported data type encountered.")
        print(traceback.format_exc())  # 输出详细的 traceback 信息
    except Exception as e:
        print("An unexpected error occurred.")
        print(traceback.format_exc())  # 输出详细的 traceback 信息

data = [10, 20, 30, 40]
a = 1

try:
    result = calculate_average(data)
    if result is not None:
        print(f"The average is {result}")
except Exception as e:
    print("An error occurred while calculating the average.")
    print(traceback.format_exc())  # 输出详细的 traceback 信息
