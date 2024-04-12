# write a progm second_largest_no in list
# remove spaces in given string
# swapping of two nos without using third variable
# print first 10 prime nos

# prime nos
result = []
for i in range(1,50):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            result.append(i)

# print(result[:10])


# Swapping nos

a = 2
b = 3

# Swap no's

# a,b = b,a

a = b + (a - a )
b = a 
print("swap values",a, b)

# print(a,b)


# remove spaces in string

str1 = "Akash Shinde"
str2 = str1.replace(" ", "")
# print(str2)


# second largest no in list

list1 = [2,3,4,5,1,9,6]
max_no = max(list1[0], list1[1])
seco_max = min(list1[0], list1[1])
for i in range(len(list1)):
    if list1[i] > max_no:
        seco_max = max_no
        max_no = list1[i]
    elif list1[i] > seco_max and max_no != list1[i]:
        seco_max = list1[i]

# print(seco_max)


str1 = input(" enter string ")

count = 0

for i in str1:
    count += 1

print("without inbuilt   ",count)

print("using inbuilt    ",len(str1))

