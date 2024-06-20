import math 
import time
import random

def partition(A, p, r):
    # Choose the middle element as the pivot
    pivot = A[r]
    
    i = p - 1     # Place for the smaller element
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]  # Swap elements
    A[i + 1], A[r] = A[r], A[i + 1]  # Swap the pivot element with the element at i+1
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)  # Partition the array
        quicksort(A, p, q - 1)  # Recursively sort the left subarray
        quicksort(A, q + 1, r)
    return A
        

def mergesort(A,p,r):
    if p < r:
        q= int(math.floor((p+r)/2))
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)
    return A

def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    
    # Create temporary arrays
    L = A[p:p + n1]
    R = A[q + 1:q + 1 + n2]
    
    i = j = 0
    k = p

    # Merge the temporary arrays back into A[p..r]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements of L[]
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements of R[]
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
        
             
def QuickSorting(A):
    # Start time
    start_time = time.time()
    p=0
    r=len(A)-1
    A=quicksort(A,p,r)
    end_time = time.time()
    time_taken=end_time - start_time
    result=[A,time_taken]
    # Return the sorted arrayay
    return result
        
def MergeSorting(A):
    A=list(A)
    start_time = time.time()
    p=int(0)
    r=len(A)-1
    S=mergesort(A,p,r)
    end_time = time.time()
    time_taken=end_time - start_time
    result=[S,time_taken]
    # Return the sorted arrayay
    return result
