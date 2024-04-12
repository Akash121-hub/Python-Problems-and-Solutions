# 11. Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations. Go to the editor
# Sample data:
# /*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
target = 70

results = []
for i in X:
    for j in Y:
        for k in Z:
            if i+j+k == target:
                results.append(list([i,j,k]))
print(results)