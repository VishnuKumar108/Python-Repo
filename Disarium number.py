# Function to check if a number is a Disarium number
def is_disarium_number(N):
    # Convert number to string to iterate over each digit
    digits = str(N)
    
    # Calculate the sum of digits raised to the power of their positions
    sum_of_powers = sum(int(digit) ** (i + 1) for i, digit in enumerate(digits))
    
    # Check if the sum is equal to the original number
    return sum_of_powers == N

# Input
N = int(input())  # Read the input number

# Output
if is_disarium_number(N):
    print("True")  # If it's a Disarium number
else:
    print("False")  # If it's not a Disarium number
