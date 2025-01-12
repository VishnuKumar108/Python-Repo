import math

def find_lcm(a, b):
    # Calculate LCM using the formula: LCM(a, b) = abs(a*b) // GCD(a, b)
    return abs(a * b) // math.gcd(a, b)

# Input
a, b = map(int, input("Enter two numbers separated by space: ").split())

# Output
print(find_lcm(a, b))
