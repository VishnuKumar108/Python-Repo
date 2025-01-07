def generate_array():
    # Read the input
    n = int(input())
    array = list(map(int, input().split()))
    
    # Initialize the result array
    result = []
    
    # Process the input array in pairs
    for i in range(0, n, 2):
        x = array[i]      # Number
        y = array[i + 1]  # Number of repetitions
        result.extend([x] * y)  # Append x repeated y times
    
    # Print the result as a space-separated string
    print(" ".join(map(str, result)))

# Example Usage
generate_array()
