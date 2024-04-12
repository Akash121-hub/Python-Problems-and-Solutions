class Solution:
    def array(self,nums):
        result = []
        for n in nums:
            n = abs(n)
            if nums[n -1] < 0:
                result.append(n)
            nums[ n - 1] = -nums[n - 1]

        return result

res = Solution()
ab = res.array([1,2,3,3,4,4])
print(ab)