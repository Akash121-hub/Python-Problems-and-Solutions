String = "AKJIOA"

result = {}

for i in String:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

frequent_val = " "
new_val = 0
for key, val in result.items():
    if val > new_val:
        new_val = val

print(new_val,key)

from collections import Counter

most_frequent = max(set(String),key=String.count)
print(most_frequent,"l")
print('The most frequent letter is, ', ["No frequent value" if String.count(most_frequent)== 1 else most_frequent,String.count(most_frequent)])

if Counter(most_frequent) == 1:
    print("No frequent value")