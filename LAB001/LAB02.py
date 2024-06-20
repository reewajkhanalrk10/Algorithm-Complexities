# Test cases for sorting algorithms
def test_sorting_algorithms():
    # Test case 1
    arr1 = [3, 2, 1, 4, 5]
    insertion_sort(arr1)
    assert arr1 == [1, 2, 3, 4, 5]

    # Test case 2
    arr2 = [5, 4, 3, 2, 1]
    selection_sort(arr2)
    assert arr2 == [1, 2, 3, 4, 5]

    # Additional test cases can be added here
