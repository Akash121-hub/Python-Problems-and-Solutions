"""
Let's understand the various ways to sort the dictionary.

Sorting by keys
Sorting by values
Sorting Algorithm
Reversing the sorted order
"""

names = {1:'Alice' ,2:'John' ,4:'Peter' ,3:'Andrew' ,6:'Ruffalo' ,5:'Chris' }  

# print(sorted(names.keys()))

# print()

# print(sorted(names.values()))

# print()



# print(sorted(names.items()))

# Sorting Algorithm
# There are various sorting algorithm to sort a dictionary; we can use other arguments in the sorted method. Let's understand the following example.

day_names = { 'one' : 'Monday' ,  'six' : 'Saturday' ,'three' : 'Wednesday' ,  'two' : 'Tuesday' , 'five': 'Friday' ,  'seven': 'Sunday' } 

number = { 'one' : 1 , 'two' : 2 , 'three' : 3 , 'four' : 4 , 'five' : 5 , 'six' : 6 , 'seven' : 7} 

print(sorted(day_names,key = number.__getitem__))

print([day_names[i] for i in sorted(day_names,key=number.__getitem__)])

# Reverse the sorted Order
# The dictionary can be reversed using the reverse argument. Let's understand the following example.

# Example -

a = {'a':2 ,'b':1 ,'c':3 ,'d':4 ,'e':5 ,'f':6 }  
print(sorted(a.values() ,  reverse= True))