def count_uncommon_elements():
    # Read input
    n, m = map(int, input().split())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))
    
    # Use sets to find unique elements
    set_a = set(array_a)
    set_b = set(array_b)
    
    # Find uncommon elements
    uncommon_elements = set_a.symmetric_difference(set_b)
    
    # Output the count of uncommon elements
    print(len(uncommon_elements))

# Example Usage
count_uncommon_elements()
