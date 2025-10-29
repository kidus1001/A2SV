# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        stack = []
        currentStr = ''
        currentNum = 0

        for ch in s:
            if ch.isdigit():
                currentNum = currentNum*10 + int(ch)
            elif ch == '[':
                stack.append((currentStr, currentNum))
                currentNum = 0
                currentStr = ''
            elif ch == ']':
                string, num = stack.pop()
                currentStr = string+currentStr*num
            else:
                currentStr += ch
        return currentStr

        """
        :type s: str
        :rtype: str
        """
        