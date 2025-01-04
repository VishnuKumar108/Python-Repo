import math

def is_perfect_square(n):
    # Calculate the square root of n
    sqrt_n = math.isqrt(n)  # math.isqrt(n) gives the integer square root of n
    # Check if the square of the integer square root is equal to n
    return sqrt_n * sqrt_n == n

# Input
n = int(input())

# Output
print(is_perfect_square(n))
