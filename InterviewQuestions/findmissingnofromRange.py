def missing_no(lst):
    n = len(lst) + 1
    actual_sum = n * (n+1) // 2
    given_lst_sum = sum(lst)
    missing_no = actual_sum - given_lst_sum
    return missing_no


result = missing_no([1,2,3,4,5,6,7,8,9,10])
print(result)