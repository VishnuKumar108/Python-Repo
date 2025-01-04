def is_pronic_number(x):
    n = 0
    while n * (n + 1) <= x:
        if n * (n + 1) == x:
            return "YES"
        n += 1
    return "NO"

# Input
x = int(input())

# Output
print(is_pronic_number(x))
