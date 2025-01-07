def uncommon_elements():
    # Read input
    n, m = map(int, input().split())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))
    
    # Use sets to find unique elements
    set_a = set(array_a)
    set_b = set(array_b)
    
    # Find uncommon elements
    uncommon = set_a.symmetric_difference(set_b)
    
    # Maintain order of first appearance in A + B
    result = [x for x in array_a + array_b if x in uncommon]
    
    # Print the uncommon elements as a space-separated string
    print(" ".join(map(str, result)))

# Example Usage
uncommon_elements()
