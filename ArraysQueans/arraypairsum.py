
def pair_sum(arr,k):
    if len(arr) < 2:
        return 
    output = set()
    seen = set()

    for num in arr:
        target = k - num
        if num not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    return output
print(pair_sum([1,3,2,2],4))

