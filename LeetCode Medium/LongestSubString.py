"""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

# s = "abcabcbb"
s = "pwwkew"
# s_l = []
# count = 0
# for i in s:
#     if i not in s_l:
#         s_l.append(i)
#         count += 1
# print(s_l, count)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test = ""
        # Result
        max_length = 0
        
        # Return zero or 1 if string is empty or only 1 length
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        for c in s:
            # If string already contains the character
            # Then substring after repeating character
            if c in test:
                test = test[test.index(c)+1:]
            test = test + c
            if max_length < len(test):
                max_length = len(test)
        return max_length