# Function to calculate the sum of squares of digits
def sum_of_squares_of_digits(n):
    return sum(int(digit) ** 2 for digit in str(n))

# Function to check if a number is a Happy Number
def is_happy_number(n):
    seen_numbers = set()  # Set to keep track of numbers we've seen
    
    while n != 1 and n != 7:
        # Calculate sum of squares of digits
        n = sum_of_squares_of_digits(n)
        
        # If we've seen this number before, we're in a cycle, so it's an unhappy number
        if n in seen_numbers:
            return False
        
        # Add the current number to the seen set
        seen_numbers.add(n)
    
    return True

# Input
N = int(input())  # Read the input number

# Output
if is_happy_number(N):
    print("True")  # If it's a Happy number
else:
    print("False")  # If it's an Unhappy number
