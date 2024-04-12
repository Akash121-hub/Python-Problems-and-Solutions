"""
2610. Convert an Array Into a 2D Array With Conditions
"""
from collections import defaultdict

class Solution:
    def findMatrix(self, nums):
        count = defaultdict(int)
        res = []
        for n in nums:
            row = count[n]
            if len(res) == row:
                res.append([])
            res[row].append(n)
            count[n] += 1
        return res

c = Solution
re = c.findMatrix()
# print(re(nums=[1,3,4,1,2,3,1]))