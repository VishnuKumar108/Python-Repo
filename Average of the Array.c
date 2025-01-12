def calculate_average(arr):
    # Calculate average
    return sum(arr) / len(arr)

# Input
n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Output
print(f"{calculate_average(arr):.2f}")
