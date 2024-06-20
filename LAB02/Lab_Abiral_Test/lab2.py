from function import generate_unsorted_array,plot_complexity
from function2 import MergeSorting,QuickSorting
from plot import plot_cases,plot_all,plot_complexity

import sys
sys.setrecursionlimit(999999999)

def question1():
    unsorted=generate_unsorted_array(10)
    print(f"Unsorted Array: {unsorted}")
    mergesort=MergeSorting(unsorted)
    print(f"Sorted Array By Merge Sort: {mergesort[0]}")
    unsorted=generate_unsorted_array(10)
    print(f"Unsorted Array: {unsorted}")
    quicksort=QuickSorting(unsorted)
    print(f"Sorted Array By Quick Sort: {quicksort[0]}")


question1()
# plot_cases(MergeSorting,"MergeSort",60000,200)
# plot_cases(QuickSorting,"QuickSort",2000,10)
# plot_complexity(QuickSorting,"QuickSort")
plot_all(4000)
