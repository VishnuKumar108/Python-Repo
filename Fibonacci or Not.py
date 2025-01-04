import math

# Function to check if a number is a perfect square
def is_perfect_square(x):
    s = int(math.isqrt(x))  # Efficient integer square root
    return s * s == x

# Function to check if the given number is a Fibonacci number
def is_fibonacci(N):
    # Check if 5*N^2 + 4 or 5*N^2 - 4 is a perfect square
    return is_perfect_square(5 * N * N + 4) or is_perfect_square(5 * N * N - 4)

# Input
N = int(input())  # Read input number

# Output
if is_fibonacci(N):
    print("True")
else:
    print("False")
