'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

'''

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            l , r = i + 1, len(nums) - 1
            while l < r:
                threesum = v + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                if threesum < 0:
                    l += 1
                else:
                    res.append([v,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

object1 = Solution()
result = object1.threeSum([1,2,3,4,5,6,7])
print(result, ".")