# """
# Here is your programming question.

# Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. 
# Update the current existing inventory item quantities (in arr1). If an item cannot be found, 
# add the new item and quantity into the inventory array. The returned inventory array should be in alphabetical order by item.
# """




def update_arr(cur_inv, new_inv):
    for i in range(len(new_inv)):
        f = False
        for j in range(len(cur_inv)):
            if new_inv[i][1] == cur_inv[j][1]:
                cur_inv[j][0] == new_inv[j][0] + new_inv[i][0]
                f = True

        if not f:
            cur_inv.append(new_inv[i])
    cur_inv = sorted(cur_inv, key = lambda a:a[1])

    return cur_inv


# first = [
# [21, "Bowling Ball"],
# [2, "Dirty Sock"],
# [1, "Hair Pin"],
# [5, "Microphone"]
# ]
# second = [
# [2, "Hair Pin"],
# [3, "Half-Eaten Apple"],
# [67, "Bowling Ball"],
# [7, "Toothpaste"]
# ]

# result = update_arr(first, second)

# print(result)