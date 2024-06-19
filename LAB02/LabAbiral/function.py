import time
import random
import matplotlib.pyplot as plt
import numpy as np
def insertionsort(array):
    # Start time
    start_time = time.time()

    # Iterate over the arrayay starting from the second element
    for i in range(1, len(array)):
        # Set the current element as the key
        key = array[i]

        # Initialize the variable j to the index of the previous element
        j = i - 1

        # Move elements of array[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < array[j]:
            # Shift the current element to the right
            array[j + 1] = array[j]
            # Move to the previous element
            j -= 1

        # Place the key at the correct position in the sorted arrayay
        array[j + 1] = key

    # End time
    end_time = time.time()
    time_taken=end_time - start_time
    result=[array,time_taken]
    # Return the sorted arrayay
    return result



def selectionsort(array):
    # Start time
    start_time = time.time()

    # Iterate over the arrayay starting from the first element
    for i in range(len(array)):
        # Assume the first unsorted element is the minimum
        min_index = i

        # Iterate over the unsorted portion of the arrayay
        for j in range(i + 1, len(array)):
            # If the current element is smaller than the current minimum
            if array[j] < array[min_index]:
                # Update the index of the minimum element
                min_index = j

        # Swap the first unsorted element with the minimum element
        array[i], array[min_index] = array[min_index], array[i]

    # End time
    end_time = time.time()
    time_taken=end_time - start_time

    result=[array,time_taken]
    # Return the sorted arrayay
    return result


def generate_unsorted_array(size):
    # Generate a list of unique integers in the range [1, size * 10]
    array = random.sample(range(1, size * 10 + 1), size)
    # Shuffle the list to make it unsorted
    random.shuffle(array)
    return array

def generate_sorted_array(size):
    # Generate a list of unique integers in the range [1, size * 10]
    array = random.sample(range(1, size * 10 + 1), size)
    return array

def get_complexity(sort):
    size=0
    x=[]
    y=[]
    while size <= 4000:
        unsorted=np.random.normal(loc=(size/2),scale=(size/4),size=size)
        # sorted_array=unsorted.copy()
        sorted=sort(unsorted)
        x.append(size)
        y.append(sorted[1])
        size =size+100
    result=[x,y]
    return result

def plot_complexity():
    insertion=get_complexity(insertionsort)
    selection=get_complexity(selectionsort)
    x=selection[0]
    y1=insertion[1]
    y2=selection[1]
    
    print(f"\nData Size: {x}\n")
    print(f"Insertion Sort Execution Time: {y1}\n")
    print(f"Selection Sort Execution Time: {y1}")
   # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    # Plot the data as a line plot
    ax.plot(x, y1, color='red', label='Insertion Sort Execution Time')
    ax.plot(x, y2, color='blue', label='Selection Sort Execution Time')
    # Set the labels for the x and y axes
    ax.set_xlabel('Array size')
    ax.set_ylabel('Time taken for sorting (seconds)')
    # Set the title of the plot
    ax.set_title('Array(Input)-size vs Sort Execution Time')
    # Add a legend to the plot
    ax.legend()
    # Display the plot
    plt.show()