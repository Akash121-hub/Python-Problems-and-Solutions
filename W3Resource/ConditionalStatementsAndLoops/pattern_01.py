"""
Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""

for i in range(5):
    print("*"*i)

for j in range(5,0,-1):
    print("*"*j)