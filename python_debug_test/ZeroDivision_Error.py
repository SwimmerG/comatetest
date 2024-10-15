def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    
    print(f"Total: {total}, Count: {count}")
    
    # Calculate the average
    average = total / count
    return average

# Test case with non-empty list
numbers1 = [2, 4, 6]
print("Average of numbers1:", calculate_average(numbers1))

# Test case with an empty list (this will cause ZeroDivisionError)
numbers2 = []
print("Average of numbers2:", calculate_average(numbers2))
