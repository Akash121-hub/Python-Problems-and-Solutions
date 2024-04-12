def binary_search(arr,target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_no = arr[middle_index]
        if middle_no == target:
            return middle_index
        if middle_no > target:
            right -= 1
        else:
            left += 1
    return -1 

print(binary_search([1,2,3,4],2))