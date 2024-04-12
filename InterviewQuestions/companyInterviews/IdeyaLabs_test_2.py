# # second largest no in arrary

# '''list5 = [1,2,20,80,100]

# first_max= max(list5[0],list5[1])
# second_max = min(list5[0],list5[1])
# for i in range(2,len(list5)):
#     if list5[i] > first_max:
#         second_max = first_max
#         first_max = list5[i]
#     elif list5[i] > second_max and first_max != list5[i]:
#         second_max = list5[i]

# print(second_max)'''

# # Reverse String

def reverse(s):
    if len(s) == 0:
            return s
    return reverse(s[1:]) + s[0]

s = reverse("AKASH")
print(s)

'''
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

s = "Geeksforgeeks"
print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))  '''

# string1 = "HELLO WORLD"

# # res = string1.split()
# # print(res)

# rev_str = " "
# for i in string1:
#     rev_str =  i + rev_str

# print(rev_str)

# stack for push and pop

# stack = []

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def Empty(self):
        return self.size == 0

    def push(self, val):
        
        node = Node(val)

        node.next = self.head.next
        self.head.next = node
        self.size += 1
        # print(node)
    
    def pop(self):
        if self.Empty():
            raise Exception (" Stack is empty")

        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1

        return remove.val

stack = Stack()


for num in range(10,20):
    stack.push(num)
print("Current stack {}".format(stack))

stack.pop()




        
        


    
        

