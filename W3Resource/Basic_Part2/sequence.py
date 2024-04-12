list1 = [1,2,3,4,4,5]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        print(False)

"""
W3 resouce code
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))
"""