list5 = [1,2,20,80,100,100,110]

first_max = max(list5[0],list5[1])
second_max = max(list5[0],list5[1])

for i in range(2,len(list5)):
    if list5[i] > first_max:
        temp = first_max
        first_max = list5[i]
        second_max = temp
    elif list5[i] > second_max and list5[i] != first_max:
        list5[i] = second_max


print(second_max)