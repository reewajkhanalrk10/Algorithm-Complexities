def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

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
        sorted_arr = quick_sort(arr)
        print(f"Sorted: {sorted_arr}\n")

# Run the tests
run_tests()
