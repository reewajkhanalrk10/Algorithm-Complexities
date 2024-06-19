def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Test cases
def run_tests():
    test_cases = [
        [],  # Empty list
        [5],  # Single element
        [3, 6, 8, 10, 1, 2, 1],  # List with duplicates
        [10, 7, 8, 9, 1, 5],  # Random list
        [5, 4, 3, 2, 1],  # Reversed list
        [1, 2, 3, 4, 5],  # Already sorted list
    ]
    
    for i, arr in enumerate(test_cases):
        print(f"Test case {i + 1}: {arr}")
        sorted_arr = merge_sort(arr)
        print(f"Sorted: {sorted_arr}\n")

# Run the tests
run_tests()
