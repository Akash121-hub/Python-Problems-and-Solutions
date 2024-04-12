# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
d = {"a":True,"a":False}
print(d)

# d = {"a":True,[1,2,3]:False}

print(d)
# d = {"a":True,(1,2,3):False}
# explain GIL lock

l = [1,9,3,4,5,6]
# output_l = [[1,2],[3,4],[5,6]]
output = []
l_len = len(l) - 1
for i in range(0,l_len,2):
        output.append([l[i],l[i+1]])
        

print(output)