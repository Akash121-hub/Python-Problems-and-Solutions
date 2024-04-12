"""# a = [1,2,3]
# b = a.copy()
# b[1] = 10
# print(a)




def func(*args, **kwargs):
    sum_args = 0
    val = list(args)
    for i in val:
        sum_args += i
    return sum_args

print(func(2,3))
print(func(1,2,3))
print(func(2,3,5,6))
print(func(2,3,5,6,7))
print(func(2,3,5,6,7,8))"""

try:
    a = 9/0
except Exception as e:
    print (e)

print("hello")

import re
regx = re.compile('[,#@]')
str1 = "Hey, Akash how are you ?? hey"
count = {}
for i in str1.split():
    if str(regx) in i:
        # print("yes")
        str(i).remove(str(regx))
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    else:
        print('/')
print(count)