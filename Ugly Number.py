def is_ugly(num):
    # Handle edge case: 1 is treated as an ugly number
    if num <= 0:
        return "Not Ugly Number"
    
    # Divide the number by 2, 3, and 5 as long as possible
    for prime_factor in [2, 3, 5]:
        while num % prime_factor == 0:
            num //= prime_factor
    
    # If num becomes 1, it means it only had factors of 2, 3, and 5
    if num == 1:
        return "Ugly Number"
    else:
        return "Not Ugly Number"

# Take input from the user
num = int(input())

# Call the function and print the result
print(is_ugly(num))
