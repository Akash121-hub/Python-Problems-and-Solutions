# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

from unittest import result


input_list = [10,20,30,40,50,60,70,80,90]

def removeEvryThirdelem(elements):
    position = 2
    idx = 0
    len_elements = len(elements)
    while len_elements > 0:
        idx = (position + idx) % len_elements
        res = elements.pop(idx)
        print(res)
        len_elements -= 1

result = removeEvryThirdelem(input_list)

print(input_list)


