
a = "Sabyasachi, Techno Exponent Techno I sabyasachi"

result = a.lower().split()
output = {}
for i in result:
    if str(i).endswith(","):
        i = i[:-1]
        output[i] = 1
    else:   
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
print(output)


