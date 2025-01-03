def add_digits(num):
    # If the number is 0, return 0
    if num == 0:
        return 0
    else:
        # Use digital root formula
        return 1 + (num - 1) % 9

# Take input from the user
num = int(input())

# Call the function and print the result
print(add_digits(num))
