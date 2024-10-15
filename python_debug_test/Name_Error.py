
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(number)  # BUG: 'number' is not defined, should be 'numbers'
    return average

data = [10, 20, 30, 40]
result = calculate_average(data)
print(f"The average is {result}")