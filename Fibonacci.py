# Function to generate and print Fibonacci series up to N terms
def fibonacci_series(N):
    a, b = 0, 1  # First two Fibonacci numbers
    fibonacci_numbers = []  # List to store Fibonacci numbers
    
    # Generate Fibonacci numbers
    for _ in range(N):
        fibonacci_numbers.append(a)  # Add the current number to the list
        a, b = b, a + b  # Update a and b to the next two Fibonacci numbers
    
    # Print all Fibonacci numbers as space-separated string
    print(" ".join(map(str, fibonacci_numbers)))

# Input
N = int(input())  # Read the number of Fibonacci numbers to generate

# Output
fibonacci_series(N)
