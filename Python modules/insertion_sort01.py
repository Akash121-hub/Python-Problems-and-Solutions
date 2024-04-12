def InsertionArray(array):
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j-1],array[j] = array[j],array[j-1]
            j -= 1

arr = [8,4,6,9,15,12,11]

InsertionArray(arr)

print(arr)


