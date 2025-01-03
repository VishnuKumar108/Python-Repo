def sum_of_divisors(n):
    # Sum the proper divisors of n (excluding n itself)
    divisors_sum = 1  # 1 is always a divisor for any n > 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def check_amicable(n, m):
    # Calculate the sum of proper divisors for both numbers
    if sum_of_divisors(n) == m and sum_of_divisors(m) == n:
        return "Amicable"
    else:
        return "Not Amicable"

# Take input from the user
n = int(input())
m = int(input())

# Call the function and print the result
print(check_amicable(n, m))
