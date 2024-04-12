"""
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
"""

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxcandies = max(candies)
        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxcandies:
                res.append(True)
            else:
                res.append(False)
        return res
res = Solution()
x = res.kidsWithCandies([2,3,5,1,3],3)
print(x)


