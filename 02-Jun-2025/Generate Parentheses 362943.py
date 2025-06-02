# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        validParenthesis = []
        def backtrack (opening, closing):
            if (opening == closing == n):
                validParenthesis.append ("".join(stack))
                return
            if (closing < opening):
                stack.append (")")
                backtrack (opening, closing+1)
                stack.pop()
            if (opening < n):
                stack.append ("(")
                backtrack (opening+1, closing)
                stack.pop()
        backtrack(0,0)
        return (validParenthesis)
        """
        :type n: int
        :rtype: List[str]
        """
        