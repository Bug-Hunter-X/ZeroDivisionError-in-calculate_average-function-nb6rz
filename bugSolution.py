def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

#Improved version with more robust error handling
def calculate_average_robust(numbers):
    if not numbers:
        return 0
    try:
        return sum(numbers) / len(numbers)
    except TypeError as e:
        print(f"Error calculating average: {e}")
        return None