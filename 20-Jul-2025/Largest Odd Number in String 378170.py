# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution(object):
    def largestOddNumber(self, num):
        revNum = num[::-1]

        i = 0
        for ch in revNum:
            toInt = int(ch)
            if toInt%2==1:
                break
            else:
                i+=1
                continue

        myI = len(num)-i

        resStr = ""
        check = 0
        while (check < myI):
            resStr += num[check]
            check+=1
        
        return resStr

        """
        :type num: str
        :rtype: str
        """
        