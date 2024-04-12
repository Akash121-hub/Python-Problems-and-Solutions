'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

'''

class Solution:
    def generateParenthesis(self, n: int):
        # only add open parantheses if open < n:
        # only add closed parantheses if closed < open
        # valid IIF open == closed == n
        stack = []
        result = []
        def trackback(openN,CloseN):
            if openN == CloseN == n:
                result.append("".join(stack))
                return
            if openN < CloseN:
                stack.append("(")
                trackback(openN+1,CloseN)
                stack.pop()
            if CloseN < openN:
                stack.append(")")
                trackback(CloseN+1,openN)
                stack.pop()
        trackback(0,0)
        return result
