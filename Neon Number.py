def is_neon_number(number):
    # Calculate the square of the number
    square_of_number = number ** 2
    
    # Calculate the sum of digits of the square
    sum_of_digits = sum(int(digit) for digit in str(square_of_number))
    
    # Check if the sum of digits is equal to the original number
    if sum_of_digits == number:
        return "Neon Number"
    else:
        return "Not Neon Number"

# Take input from the user
N = int(input())

# Call the function and display the result
result = is_neon_number(N)
print(result)
