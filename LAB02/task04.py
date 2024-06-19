import time
import random
import matplotlib.pyplot as plt

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
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

# Function to generate random input
def generate_random_input(size):
    return [random.randint(800, 1200) for _ in range(size)]  # Adjusted range to have less gaps around 1000

# Function to measure execution time of sorting algorithms
def measure_execution_time(sort_function, arr, *args):
    start_time = time.time()
    sort_function(arr, *args)
    end_time = time.time()
    return end_time - start_time

# Number of test cases
num_test_cases = 10

# Fixed array size for all test cases
array_size = 100

# Lists to store execution times for each sorting algorithm
insertion_times = []
selection_times = []
quick_times = []
merge_times = []

# Perform test cases
for _ in range(num_test_cases):
    # Generate random input for each test case
    data = generate_random_input(array_size)
    
    # Measure insertion sort execution time
    insertion_data = data.copy()
    insertion_time = measure_execution_time(insertion_sort, insertion_data)
    insertion_times.append(insertion_time)
    
    # Measure selection sort execution time
    selection_data = data.copy()
    selection_time = measure_execution_time(selection_sort, selection_data)
    selection_times.append(selection_time)
    
    # Measure quick sort execution time
    quick_data = data.copy()
    quick_time = measure_execution_time(quick_sort, quick_data, 0, len(quick_data) - 1)
    quick_times.append(quick_time)
    
    # Measure merge sort execution time
    merge_data = data.copy()
    merge_time = measure_execution_time(merge_sort, merge_data)
    merge_times.append(merge_time)

# Plot input size vs. execution time for all sorting algorithms
plt.plot(range(1, num_test_cases + 1), insertion_times, label='Insertion Sort')
plt.plot(range(1, num_test_cases + 1), selection_times, label='Selection Sort')
plt.plot(range(1, num_test_cases + 1), quick_times, label='Quick Sort')
plt.plot(range(1, num_test_cases + 1), merge_times, label='Merge Sort')
plt.xlabel('Test Case')
plt.ylabel('Execution Time (s)')
plt.xticks(range(1, num_test_cases + 1))
plt.title('Execution Time for Sorting Algorithms (Array Size: 100)')
plt.legend()
plt.show()
