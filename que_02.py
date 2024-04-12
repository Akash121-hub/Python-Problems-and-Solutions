"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Go to the editor 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String 
"""

def get_firstTwo_and_lasTwo_char(str1):
    if len(str1) > 2:
        characs = str1[:2] + str1[-2:]
        return characs
    else:
        print("Empty String")

print(get_firstTwo_and_lasTwo_char("w3resource"))

str1 = "GoodMorning"
print(str1[2:4],str1.count(str1[2:4]))


class Employee:
    def __init__(var,id,name):
        var.id = id
        var.name = name
    
    def print_emp_id(var):
        print(var.id,var.name)

obj = Employee("akash",90)
obj.print_emp_id()

str1 = "1Akash1"

if str1[0].isdigit():
    print("yes")
    
import re

if re.match(r"\d",str1):
    print("yes")