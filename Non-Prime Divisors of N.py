def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_non_prime_divisors(n):
    non_prime_count = 0
    for i in range(1, n + 1):
        if n % i == 0:  # i is a divisor of n
            if not is_prime(i):  # i is not a prime
                non_prime_count += 1
    return non_prime_count

# Input
n = int(input())

# Output
print(count_non_prime_divisors(n))
