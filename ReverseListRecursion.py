
def reverse_list(lst,l,r):
    if l >= r:
        return lst
    temp = lst[l]
    lst[l] = lst[r]
    lst[r] = temp
    return (lst,l+1,r-1)
my_list = [1,2,3,4,5]
left = 0
right = len(my_list) - 1

print(reverse_list(my_list,left,right))