# Assume this script is named 'script.py'

# Importing a module that doesn't exist
import non_existent_module

def greet():
    print("Hello, welcome to the program!")

def calculate_sum(a, b):
    return a + b

# Call the functions
greet()
result = calculate_sum(5, 10)
print(f"The sum is: {result}")

# This part will never be reached due to the ImportError above
print("This won't be printed because of the ImportError.")
