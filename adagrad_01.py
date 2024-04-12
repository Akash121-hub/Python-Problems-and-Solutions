# stocks = [100,80,60,70,60,75,86]
# span = [1,1,1,2,1,4,6]

# class Stocks:
#     def __init__(self):
#         self.stck = []
    
#     def next(self,price):
#         day = 1
#         while self.stck and self.stck[-1][0] <= price:
#             day += self.stck.pop()[-1]
#         self.stck.append((price,day))

#         return day



# obj = Stocks()
# print(obj.next(100))

def stocks(price,day,s):

    for i in range(1,day,1):
        



def moneydistribut(money,children):
    
    money -= children

    if money < 0:
        return -1
    cnt = money // 7
    remain = money % 7

    if cnt == children and remain == 0 :
        return cnt

    if cnt == children - 1 and remain == 3:
        return cnt - 1
    
    return min(children - 1, cnt)

print(moneydistribut(16,2))
    