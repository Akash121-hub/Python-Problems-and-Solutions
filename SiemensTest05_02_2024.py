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