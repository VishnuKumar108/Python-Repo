def sum_of_even_indexed(arr):
    # Sum elements at even indices
    return sum(arr[i] for i in range(0, len(arr), 2))

# Input
n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Output
print(sum_of_even_indexed(arr))
