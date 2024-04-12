# print firt twenty prime nos

def check_prime(num):
    if num <= 1:
        return 1
    for i in range(2,int(num**0.5)):
        if num  % i == 0:
            return False
    return True

def first_twenty(range_of_nos):
    number = 2
    results = []
    while len(results) <= range_of_nos:
        if check_prime(number):
            results.append(number)
        number += 1
    return (results)

res = first_twenty(20)
print(res)
