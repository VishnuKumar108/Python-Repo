def is_prime(num):
    """Check if a number is a prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def average_of_primes(array):
    """Calculate the average of prime numbers in an array."""
    primes = [num for num in array if is_prime(num)]
    if not primes:
        return 0.00
    return sum(primes) / len(primes)

# Input
n = int(input())
if n == 0:
    print("0.00")
else:
    array = list(map(int, input().split()))
    average = average_of_primes(array)
    print(f"{average:.2f}")
