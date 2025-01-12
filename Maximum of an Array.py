def find_maximum(arr):
    # Use Python's built-in max function to find the maximum element
    return max(arr)

# Input
n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Output
print(find_maximum(arr))
