"""Write a Python program that removes and prints every third number from a list of numbers until the list is empty."""

list1 = [1,23,49,4,5,4,45,9,90,92,898]
# removed_elements = []
# for i in range(len(list1)):
#     while i == 3:
#         print(list1[i])
#         list1.remove(list1[i])
    

def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    # print(idx)
    print(int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)
