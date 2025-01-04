
# Function to check if a number is palindrome
def is_palindrome(n):
    # Convert the number to a string and compare with its reverse
    return str(n) == str(n)[::-1]

# Input
n = int(input())  # Read the input number

# Output
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
