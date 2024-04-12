arr = [10,10,20,20,20,30,30,40,40,40]
# Output: {10: 2, 20: 3, 30: 2, 40: 3}

values = {}

for i in arr:
    if i in values:
        values[i] += 1
    else:
        values[i] = 1

# print(values)

a = [1,2,3]
b = [1,2]

c = []

for i in a:
    if i in b:
        c.append(i)

# print(c)

num = 4

factorial = 1
for i in range(1,num+1):
    factorial = factorial * i

# print(factorial) 

print(bool("False"))

print(range(1,10))
print(range(1,10,2))

tup = (1,[2,3,4],4,"world")
# tup[2] = 90
print(type(tup))
print(tup[:])
print("############################")
print("abc" < "abcd")