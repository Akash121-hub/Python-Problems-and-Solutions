# write a program to get the vowels ( a,e,i,o,u)
# Shinde -> Shendi

input1 = "Shinde"
vowels = ""

# output = ""
for i in input1:
    if i in "aeiou":
        vowels +=i

result = ""
for j in input1:
    if j in "aeiou":
        result += vowels[-1]
        vowels = vowels[:-1]
    else:
        result += j
print(result)

        

