def is_even_array(arr):
    # Check if all elements in the array are even
    return all(x % 2 == 0 for x in arr)

# Input
n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Output
print(is_even_array(arr))
