"""
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class ClimbingStairs:
    def solutin(self, n):
        one, two = 1,1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

res = ClimbingStairs()
re = res.solutin(5)
print(re)
             
