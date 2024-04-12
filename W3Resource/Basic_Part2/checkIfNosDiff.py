"""1. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other."""

# def func(sequence):
#     pairs = {}
#     for i in sequence:        
#         if i not in pairs:
#             pairs[i] = 1
#         else:
#             pairs[i] += 1
#     for val in pairs.values():
#         if val > 1: 
#             print(False)
#         else:
#             print(True)

# print(func([1,2,3,4,5,5]))


def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))