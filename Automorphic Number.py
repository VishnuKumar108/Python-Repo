def is_automorphic(n):
    # Compute the square of the number
    square = n * n
    
    # Check if the square ends with the original number
    if str(square).endswith(str(n)):
        return "Automorphic Number"
    else:
        return "Not an Automorphic Number"

# Take input from the user
n = int(input())

# Call the function and print the result
print(is_automorphic(n))
