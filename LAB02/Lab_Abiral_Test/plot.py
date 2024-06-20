from function import get_complexity,selectionsort,insertionsort,generate_sorted_array,generate_unsorted_array
from function2 import QuickSorting,MergeSorting
import matplotlib.pyplot as plt
import numpy as np

def plot_complexity(sort,name):
 
    sorted=get_complexity(sort)
    
    x=sorted[0]
    y=sorted[1]
    
    print(f"\nData Size: {x}\n")
    print(f"{name} Execution Time: {y}\n")
   # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    # Plot the data as a line plot
    ax.plot(x, y, color='blue', label=f'{name}Execution Time')
    # Set the labels for the x and y axes
    ax.set_xlabel('Array size')
    ax.set_ylabel('Time taken for sorting (seconds)')
    # Set the title of the plot
    ax.set_title(f'Array(Input)-size vs {name} Execution Time')
    # Add a legend to the plot
    ax.legend()
    # Display the plot
    plt.show()
    

def plot_cases(sort,name,n,i):
    size=0
    best= list()
    worst=list ()
    x=[]
    y1=[]
    y2=[]
    y3=[]
    while size <= n:
        unsorted=generate_unsorted_array(size)
        sorted=[x for x in range(0,size)]
        reverse=[x for x in range(size,0,-1)]
        best_sort=sort(sorted)
        worst_sort=sort(reverse)
        average_sort=sort(unsorted)
        x.append(size)
        y1.append(best_sort[1])
        y2.append(worst_sort[1])
        y3.append(average_sort[1])
        size+=i

   # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    # Plot the data as a line plot
    ax.plot(x, y1, color='blue', label=' Sorted Array Sorting Time')
    ax.plot(x, y2, color='red', label='Reversed Array Sorting Time')
    ax.plot(x, y3, color='green', label='Normal Array Sorting Time')
    # Set the labels for the x and y axes
    ax.set_xlabel('Array size')
    ax.set_ylabel('Time taken for sorting (seconds)')
    # Set the title of the plot
    ax.set_title(f'Array(Input)-size vs {name} Execution Time')
    # Add a legend to the plot
    ax.legend()
    # Display the plot
    plt.show()


def plot_all(size):
    sizes=0
    worst=list ()
    x=[]
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    while sizes<= size :
        worst=np.random.normal(loc=(sizes/2),scale=(sizes/4),size=sizes)
        worst_sort1=insertionsort(worst)
        worst_sort2=selectionsort(worst)
        worst_sort3=MergeSorting(worst)
        worst_sort4=QuickSorting(worst)
        x.append(sizes)
        y1.append(worst_sort1[1])
        y2.append(worst_sort2[1])
        y3.append(worst_sort3[1])
        y4.append(worst_sort4[1])
        sizes +=100

   # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    # Plot the data as a line plot
    ax.plot(x, y1, color='red', label=f' InsertionSort Time Taken')
    ax.plot(x, y2, color='blue', label=f'SelectionSort Time Taken')
    ax.plot(x, y3, color='green', label=f'MergeSort Time Taken')
    ax.plot(x, y4, color='black', label=f'QuickSort Time Taken')
    # Set the labels for the x and y axes
    ax.set_xlabel('Array size')
    ax.set_ylabel('Time taken for sorting (seconds)')
    # Set the title of the plot
    ax.set_title(f'Array(Input)-size vs Sort Execution Time')
    # Add a legend to the plot
    ax.legend()
    # Display the plot
    plt.show()