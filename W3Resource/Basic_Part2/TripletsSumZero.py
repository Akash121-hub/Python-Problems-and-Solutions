# Write a Python program to identify unique triplets whose three elements sum to zero from an array of n integers.

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]

# found = False
# for i in range(0,len(x) - 2 ):
#     for j in range(i+1, len(x) - 1):
#         for k in range(j+1,len(x)):
#             if x[i]+x[j]+x[k] == 0:
#                 print(x[i],x[j],x[k])
#                 found = False
            
# if (found == False):
#         print(" not exist ")              


# python program to find triplets in a given
# array whose sum is zero
 
# function to print triplets with 0 sum
 
 
def findTriplets(arr, n):
 
    found = False
 
    # sort array elements
    arr.sort()
 
    for i in range(0, n-1):
 
        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):
 
            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                found = True
 
            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l += 1
 
            # if sum is greater than zero then
            # decrement in right side
            else:
                r -= 1
 
    if (found == False):
        print(" No Triplet Found")
 
 
# Driven source
arr = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
n = len(arr)
findTriplets(arr, n)