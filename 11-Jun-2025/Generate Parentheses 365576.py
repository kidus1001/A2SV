# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def backTrack (open, close, possible):
            if (open == close == n):
                result.append("".join(possible))
                return
            if (open>n or close > n):
                return
            if (open<n):
                possible.append('(')
                backTrack(open+1, close, possible)
                possible.pop()
            if (close < open):
                possible.append(')')
                backTrack(open, close+1, possible)
                possible.pop()
        backTrack (0,0,[])
        return result


        """
        :type n: int
        :rtype: List[str]
        """
        