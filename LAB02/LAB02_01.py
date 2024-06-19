# Import necessary modules
import time
import random
import matplotlib.pyplot as plt
from LAB01 import selection_sort, insertion_sort 

# Function to generate random input array of given size
def generate_random_input(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to measure execution time of a sorting algorithm
def measure_execution_time(sort_function, arr):
    start_time = time.time()  # Record start time
    sort_function(arr)  # Execute the sorting function
    end_time = time.time()  # Record end time
    return end_time - start_time  # Calculate and return the elapsed time

# List of different input sizes to test the algorithms with
sizes = [1000, 2000, 3000, 4000, 5000]
# Lists to store execution times for insertion sort and selection sort
insertion_times = []
selection_times = []

# Measure execution time for each input size
for size in sizes:
    data = generate_random_input(size)  # Generate random input data
    
    # Measure and store insertion sort execution time
    insertion_data = data.copy()  # Copy data to avoid in-place sorting issues
    insertion_time = measure_execution_time(insertion_sort, insertion_data)
    insertion_times.append(insertion_time)
    
    # Measure and store selection sort execution time
    selection_data = data.copy()  # Copy data to avoid in-place sorting issues
    selection_time = measure_execution_time(selection_sort, selection_data)
    selection_times.append(selection_time)

# Plot input size vs. execution time for both sorting algorithms
plt.plot(sizes, insertion_times, label='Insertion Sort')
plt.plot(sizes, selection_times, label='Selection Sort')
plt.xlabel('Input Size')  # Label for the x-axis
plt.ylabel('Execution Time (s)')  # Label for the y-axis
plt.title('Input Size vs. Execution Time for Sorting Algorithms')  # Plot title
plt.legend()  # Display legend
plt.show()  # Show the plot

# LAB01 codes for sorting algorithms with comments

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # Element to be positioned
        j = i - 1  # Compare with elements before it
        while j >= 0 and key < arr[j]:  # Shift elements to the right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place the key in its correct position

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):  # Iterate over the entire array
        min_idx = i  # Assume the current position is the minimum
        for j in range(i + 1, len(arr)):  # Find the minimum element in the unsorted part
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the minimum element's index
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the found minimum with the first element
