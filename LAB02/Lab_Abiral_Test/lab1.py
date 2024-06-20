from function import selectionsort, insertionsort,plot_complexity,generate_unsorted_array,plot_complexity


def question1():
    unsorted=generate_unsorted_array(10)
    print(f"Unsorted Array: {unsorted}")
    insertion=insertionsort(unsorted)
    print(f"Sorted Array By Insertion: {insertion[0]}")
    unsorted=generate_unsorted_array(10)
    print(f"Unsorted Array: {unsorted}")
    selection=selectionsort(unsorted)
    print(f"Sorted Array By Selection: {selection[0]}")


question1()
plot_complexity()