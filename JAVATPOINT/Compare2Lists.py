import collections
import functools  

"""
list1 = [10,20,30,40,50]
list2 = [10,20,30,40,50]

if collections.Counter(list1) == collections.Counter(list2):
    print("both lists are same")
else:
    print("Both lists are not same")

"""
"""
The reduce() and map()
The map() function accepts a function and Python iterable object (list, tuple, string, etc) as an arguments and returns a map object. The function implements to each element of the list and returns an iterator as a result.

Besides, The reduce() method implements the given function to the iterable object recursively.

Here, we will use both methods in combination. The map() function would implement the function (it can be user-define or lambda function) to every iterable object and the reduce() function take care of that would apply in recursive manner.
"""

list1 = [10, 20, 30, 40, 50]  
list2 = [10, 20, 30, 50, 40, 60, 70]  
list3 = [10, 20, 30, 40, 50]  

if functools.reduce(lambda x,y:x and y,map(lambda a,b:a == b,list1,list2), True):
    print("list1 and list2 are equal")
else:
    print("list1 and list2 are not equal")

if functools.reduce(lambda x,y:x and y, map(lambda a,b:a == b, list1,list3)):
    print("list1 and list2 are equal")
else:
    print("list1 and list2 are not equal")


"""
The set() function and == operator
Python set() function manipulate the list into the set without taking care of the order of elements. Besides, we use the equal to operator (==) to compare the data items of the list. Let's understand the following example.

Example -

list1 = [11, 12, 13, 14, 15]  
list2 = [12, 13, 11, 15, 14]  
  
a = set(list1)  
b = set(list2)  
  
if a == b:  
    print("The list1 and list2 are equal")  
else:  
    print("The list1 and list2 are not equal")  
"""