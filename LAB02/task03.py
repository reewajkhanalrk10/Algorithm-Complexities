import time
import random
import matplotlib.pyplot as plt

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Merge Sort Implementation
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

# Function to generate random input array of given size
def generate_random_input(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to measure execution time of a sorting algorithm
def measure_execution_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Function to generate best case input for Quick Sort
def generate_quick_sort_best_case(size):
    return list(range(1, size+1))

# Function to generate worst case input for Quick Sort
def generate_quick_sort_worst_case(size):
    return list(range(size, 0, -1))

# Function to plot best and worst case execution times for Quick Sort and Merge Sort
def plot_best_worst_case():
    quick_sort_best_case_times = []
    quick_sort_worst_case_times = []
    merge_sort_best_case_times = []
    merge_sort_worst_case_times = []

    for size in sizes:
        # Best case for Quick Sort
        quick_sort_best_case_data = generate_quick_sort_best_case(size)
        quick_sort_best_case_time = measure_execution_time(quick_sort, quick_sort_best_case_data)
        quick_sort_best_case_times.append(quick_sort_best_case_time)

        # Worst case for Quick Sort
        quick_sort_worst_case_data = generate_quick_sort_worst_case(size)
        quick_sort_worst_case_time = measure_execution_time(quick_sort, quick_sort_worst_case_data)
        quick_sort_worst_case_times.append(quick_sort_worst_case_time)

        # Best case for Merge Sort
        merge_sort_best_case_data = quick_sort_best_case_data.copy()  # Merge Sort behaves the same for all cases
        merge_sort_best_case_time = measure_execution_time(merge_sort, merge_sort_best_case_data)
        merge_sort_best_case_times.append(merge_sort_best_case_time)

        # Worst case for Merge Sort
        merge_sort_worst_case_data = quick_sort_worst_case_data.copy()  # Merge Sort behaves the same for all cases
        merge_sort_worst_case_time = measure_execution_time(merge_sort, merge_sort_worst_case_data)
        merge_sort_worst_case_times.append(merge_sort_worst_case_time)

    # Plot best and worst case execution times
    plt.figure(figsize=(12, 6))

    # Quick Sort
    plt.subplot(1, 2, 1)
    plt.plot(sizes, quick_sort_best_case_times, label='Best Case')
    plt.plot(sizes, quick_sort_worst_case_times, label='Worst Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Quick Sort: Best and Worst Case Execution Times')
    plt.legend()

    # Merge Sort
    plt.subplot(1, 2, 2)
    plt.plot(sizes, merge_sort_best_case_times, label='Best Case')
    plt.plot(sizes, merge_sort_worst_case_times, label='Worst Case')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Merge Sort: Best and Worst Case Execution Times')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Measure execution times for different input sizes
sizes = [1000, 2000, 3000, 4000, 5000]
quick_sort_times = []
merge_sort_times = []

for size in sizes:
    data = generate_random_input(size)
    
    quick_sort_time = measure_execution_time(quick_sort, data.copy())
    quick_sort_times.append(quick_sort_time)
    
    merge_sort_time = measure_execution_time(merge_sort, data.copy())
    merge_sort_times.append(merge_sort_time)

# Plot input size vs. execution time
plt.plot(sizes, quick_sort_times, label='Quick Sort')
plt.plot(sizes, merge_sort_times, label='Merge Sort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (s)')
plt.title('Input Size vs. Execution Time for Quick Sort and Merge Sort')
plt.legend()
plt.show()

# Plot best and worst case execution times for Quick Sort and Merge Sort
plot_best_worst_case()
