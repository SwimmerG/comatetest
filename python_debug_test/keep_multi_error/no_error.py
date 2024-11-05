def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both arguments must be numbers."
    return result

def main():
    numbers = [(10, 2), (5, 0), ('a', 3), (8, 4)]
    for num1, num2 in numbers:
        print(f"Dividing {num1} by {num2} gives: {divide_numbers(num1, num2)}")

if __name__ == "__main__":
    main()