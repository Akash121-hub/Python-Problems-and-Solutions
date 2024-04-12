# def Threesum(arr,val):
#     res = []
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             for k in range(j+1,len(arr)):
#                 if i+j+k == val:
#                     res.append([i,j,k])
#     return res


# result = Threesum([2,3,4,5,6,7,8,1],16)

# print(result)

# a = [1,2,3,4,5]
# print(len(a)//2)

# a = 5000

# b = a//10

# print(b % 10)
'''
l = [1,2,3,4,5]
value = []
# value = [x&1 for x in l]
for x in l:
    a = 1&x
    # print(a)
    value.append(a)
print(value) '''
'''
*
**
***
****'''
"""list2 = [2,0,4,1,7,1]
for i in range(len(list2)):
    for j in range(i+1,len(list2)):
        if list2[i] > list2[j]:
            list2[i],list2[j] = list2[j], list2[i]
print(list2)"""



def twosum2(nums,target):
    for i in range(len(nums)):
        for j in range(len((i+1,nums))):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i,j]

a = twosum2([2,7,3,6,2], 9)
print(a)

