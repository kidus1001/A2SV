# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        stack = []
        if not s:
            return ""
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else: 
                intermediateRes = []
                while stack[-1] != '[':
                    intermediateRes.append(stack.pop())
                stack.pop()
                numStr = []
                while stack and stack[-1].isdigit():
                    numStr.append(stack.pop())
                numStr.reverse()
                if numStr:
                    num = int("".join(numStr))
                else:
                    num = 1
                res = "".join(intermediateRes)
                res = res[::-1]

                for ch in res * num:
                    stack.append(ch)

        return "".join(stack)
        """
        :type s: str
        :rtype: str
        """
        