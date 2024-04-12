"""
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
"""
class Solution:
    def arraystrings(self,word1,word2):
        m, n = 0, 0
        result = []

        while m < len(word1) and n < len(word2):
            result.append(word1[m])
            result.append(word2[n])
            m += 1
            n += 1
        result.append(word1[m:])
        result.append(word2[n:])
        return "".join(result)

abc = Solution()
re = abc.arraystrings("abc","pqr")
print(re)

