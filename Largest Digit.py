def largest_digit(n):
    n_str = str(n)
    max_digit = max(n_str)
    return max_digit
n = int(input())
print(largest_digit(n))
