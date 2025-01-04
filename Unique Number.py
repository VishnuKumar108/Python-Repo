def check_unique_number(n):
    # Convert the number to a string to check each digit
    n_str = str(n)
    
    # Use a set to track digits we have already encountered
    seen_digits = set()
    
    # Loop through each digit in the number
    for digit in n_str:
        # If the digit is already in the set, it's a duplicate
        if digit in seen_digits:
            return "Not Unique Number"
        # Add the digit to the set
        seen_digits.add(digit)
    
    # If no duplicates were found
    return "Unique Number"

# Input
n = int(input())

# Output
print(check_unique_number(n))
