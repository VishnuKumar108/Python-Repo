def sum_of_evens(arr):
    # Filter and sum only even numbers
    return sum(x for x in arr if x % 2 == 0)

# Input
n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Output
print(sum_of_evens(arr))
