"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def arrange_pivot(array, i, n):
    pivot = array[n]
    while(n):
        if array[i] > pivot:
            array[n] = array[i]
            array[i] = array[n-1]
            array[n-1] = pivot
            n = n-1
        elif array[i] < pivot:
            i = i+1
            
        else:
            break
    
    return n
def sort_items(array, i,n):
    if i>=n:
        return
    pivot_index = arrange_pivot(array,i,n)
    sort_items(array, i, pivot_index-1)
    sort_items(array, pivot_index+1,n)
def quicksort(array):
    sort_items(array,0, len(array)-1)
    return array
    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)