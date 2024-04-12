"""
1. Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False
"""

Input1 = [19, 19, 15, 5, 3, 5, 2]
dictinry = {}
# for i in Input1:
#     if i in dictinry:
#         dictinry[i] += 1
#     else:
#         dictinry[i] = 1
# print(dictinry)
# for key, val in dictinry.items():
#     # print(type(key), type(val))
#     if (key == 19 and val == 2):
        
#     # else:
#     #     continue
    
if Input1.count(19) == 2 and Input1.count(5) >= 3:
    print(True)

else:
    print(False)