# Function to calculate the sum of proper divisors
def sum_of_divisors(n):
    sum_divisors = 0
    # Iterate over possible divisors from 1 to n//2
    for i in range(1, n // 2 + 1):
        if n % i == 0:  # If i is a divisor
            sum_divisors += i
    return sum_divisors

# Function to check if a number is abundant
def is_abundant_number(n):
    # Get the sum of proper divisors
    sum_divs = sum_of_divisors(n)
    
    # Check if sum of divisors is greater than the number
    return sum_divs > n

# Input
N = int(input())  # Read the input number

# Output
if is_abundant_number(N):
    print("True")  # If it's an abundant number
else:
    print("False")  # If it's not an abundant number
