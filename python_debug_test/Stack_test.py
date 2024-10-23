def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(x, y):
    sum_result = add(x, y)
    product_result = multiply(x, y)
    print(f"Sum: {sum_result}, Product: {product_result}")

def main():
    calculate(5, 3)

main()
# Output: