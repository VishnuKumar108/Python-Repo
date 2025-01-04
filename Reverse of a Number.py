def reverse_number(n):
    # Convert the number to a string, reverse it, and then convert back to an integer
    reversed_n = str(n)[::-1]
    return reversed_n

# Input
n = int(input())

# Output
print(reverse_number(n))
