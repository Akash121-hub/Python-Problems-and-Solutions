remove_dup = "AKASH"

new_str = ""

for i in remove_dup:
    if i not in new_str:
        new_str = new_str + i
        
print(new_str)
print("".join(str(set(remove_dup))))