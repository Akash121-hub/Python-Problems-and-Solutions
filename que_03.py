"""4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor 
Sample String : 'restart'
Expected Result : 'resta$t'"""
'''
def change_char(str1):
    char_1 = str1[0]
    for i in str1:
        if i == char_1:
            result = char_1 + ( str1[1:].replace(i,"$") )
    return result


d1= {"a":40, "peter":45}
d2= {"a":466, "peter":45}
str2 = "restart"
# k = [print(i) for i in str2 if i not in "aeiou"]

a = { }
a[1] = 1
a['1'] = 2
a[1.0] = 4
count = 0
for i in a:
    count += a[i]
print(count)

x= input("enter num: ")
print(type(x))

# D = {1:{1:"A"}, 2:"B"}, 3:"C", 'B':"D", "D":'E'}

x = ['Training', 'Online', 'Mode']
print(list(map(x.upper(), x))) '''

# from calendar import c
# from distutils.log import error
# import itertools
# from re import A
# from this import d
# # print(list(itertools.takewhile(lambda x:x < 100, [90,11,26,300,101])))

x = [3,4], (4,7,7), {7,11,7,11,13}

s = list(map(sum, x))
print(s)

"""
def fun(a):
    return a +fun(a-2)

print(fun(8))"""

'''
string_ex = "aabbccdd"
new_str = ""
for i in string_ex:
    if i not in new_str:
        new_str =  i + new_str
print(new_str) 

'''

'''
ex_dict = {'a':10,'b':20,'c':10,'d':100}

search_key = input("enter key to search:  ")

if search_key in ex_dict.keys():
    print("Key found", ex_dict[search_key])
else:
    print("key not found") '''


find_freq_value = "AKASH"
new_dict = {}
for i in find_freq_value:
    if i not in new_dict:
        new_dict[i] = 1
    else:
        new_dict[i] += 1

# for i, j in new_dict.items():
# result = max(new_dict, key=lambda x:new_dict[x])
result = max(new_dict, key= lambda x:new_dict[x])
print(result)
# print(new_dict)


