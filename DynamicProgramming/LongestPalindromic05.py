"""
5. Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longest_palindrome(self,str1):
        res = ""
        resLen = 0
        for i in range(len(str1)):
            l,r = i,i
            while i >= 0 and r < len(str1) and str1[l] == str1[r]:
                if (r - l + 1) > resLen:
                    res = str1[l:r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1
            l,r = i, i + 1

            while i >= 0 and r < len(str1) and str1[l] == str1[r]:
                if (r - l + 1) > resLen:
                    res = str1[l:r+1]
                    resLen = (r - l + 1)
                l -= 1
                r += 1    
        return res

obj = Solution()
result = obj.longest_palindrome("ababc")
print(result)