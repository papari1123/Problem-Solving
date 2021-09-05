"""
1. Insert Sort
- use the key A[i] for sorted array A[0, ... , i-1].
- find the right postion (j) of A[i].
ref : https://www.geeksforgeeks.org/insertion-sort/
ref : https://www.geeksforgeeks.org/merge-sort/
"""

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1 
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Driver code to test above
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    print(arr)
    arr2 = [12, 11, 13, 5, 6]
    mergeSort(arr2)
    print(arr2)
    