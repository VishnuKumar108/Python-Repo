def reverse_integer(n):
    # Define the 32-bit signed integer limits
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    
    # Check if the number is negative
    is_negative = n < 0
    n = abs(n)  # Work with the absolute value
    
    # Reverse the digits of the number
    reversed_num = int(str(n)[::-1])
    
    # If the number was negative, restore the negative sign
    if is_negative:
        reversed_num = -reversed_num
    
    # Check for overflow
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0
    
    return reversed_num

# Take input from the user
n = int(input())

# Call the function and print the result
print(reverse_integer(n))
