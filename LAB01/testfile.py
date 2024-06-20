import time
import random
import matplotlib.pyplot as plt
from LAB01 import selection_sort, insertion_sort 


# Function to generate random input
def generate_random_input(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to measure execution time of sorting algorithms
def measure_execution_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Perform sorting and measure execution time for both algorithms
sizes = [1000, 2000, 3000, 4000, 5000]
insertion_times = []
selection_times = []

for size in sizes:
    data = generate_random_input(size)
    
    # Measure insertion sort execution time
    insertion_data = data.copy()
    insertion_time = measure_execution_time(insertion_sort, insertion_data)
    insertion_times.append(insertion_time)
    
    # Measure selection sort execution time
    selection_data = data.copy()
    selection_time = measure_execution_time(selection_sort, selection_data)
    selection_times.append(selection_time)

# Plot input size vs. execution time
plt.plot(sizes, insertion_times, label='Insertion Sort')
plt.plot(sizes, selection_times, label='Selection Sort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (s)')
plt.title('Input Size vs. Execution Time for Sorting Algorithms')
plt.legend()
plt.show()
