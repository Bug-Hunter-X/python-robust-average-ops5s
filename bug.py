def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage that can cause ZeroDivisionError
average = calculate_average([])  #Should return 0, but this might cause a crash
print(average)