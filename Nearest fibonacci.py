def nearest_fibonacci(n):
    # Handle the case when n is 0 or 1 directly
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Generate Fibonacci numbers up to the given number n
    fib1, fib2 = 0, 1
    fib_list = [fib1, fib2]
    
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib2)
    
    # Compare the last two Fibonacci numbers with the input number n
    diff1 = abs(fib_list[-2] - n)
    diff2 = abs(fib_list[-1] - n)
    
    if diff1 < diff2:
        return fib_list[-2]
    elif diff2 < diff1:
        return fib_list[-1]
    else:
        return fib_list[-2], fib_list[-1]  # If both distances are equal

# Take input from the user
n = int(input())

# Call the function and print the result
result = nearest_fibonacci(n)
if isinstance(result, tuple):
    print(" ".join(map(str, result)))
else:
    print(result)
