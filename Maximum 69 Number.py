def maximum_69_number(n):
    # Convert the number to a string for easy manipulation
    num_str = str(n)
    
    # Try to find the first occurrence of '6' and change it to '9'
    for i in range(len(num_str)):
        if num_str[i] == '6':
            # Create the new number with '6' changed to '9'
            num_str = num_str[:i] + '9' + num_str[i+1:]
            break
    
    # Convert the modified string back to an integer and return it
    return int(num_str)

# Take input from the user
n = int(input())

# Call the function and print the result
print(maximum_69_number(n))
