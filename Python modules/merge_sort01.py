# Merge sort is divide and conquer algorithm 
# Merge sory first divides the list into equal parts and then unites them as a sorted list

# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         L = arr[:mid]
 
#         # Into 2 halves
#         R = arr[mid:]
 
#         # Sorting the first half
#         mergeSort(L)
 
#         # Sorting the second half
#         mergeSort(R)
 
#         i = j = k = 0
 
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
 
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
 
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#         print(arr)
# lst =[2,8,5,4]
# mergeSort(lst)
"""
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
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
        print(arr)
# MergeSort()

lst =[2,8,5,4]
mergeSort(lst)
# print(lst)

"""

def MergeSort(array):
    mid = len(array)
    L = array[:mid]
    R = array[:mid]

    if len(array) > 1:
        i = 0
        j = 0
        k = 0
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        print(array)
        # while i < len(L) and j < len(R):
        #     if L[i] <= R[j]:
        #         array[k] = L[i]
        #         i += 1
            
        # while i < len(L):
        #     array[k] = L(i)
        #     i += 1
        #     k += 1
        
        # while j < len(R):
        #     array[k] = R[j]
        #     j+= 1
        #     k += 1




MergeSort([4,3,2,1])
