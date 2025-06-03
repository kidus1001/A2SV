# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        if (x<0):
            return False
        numList = []
        while (x > 0):
            singleDigitNum = x % 10
            x /= 10
            numList.append(singleDigitNum)
        left = 0
        right = len(numList)-1
        while (left < right):
            if(numList[left] != numList[right]):
                return False
            left+=1
            right-=1
        
        return True
        
        """
        :type x: int
        :rtype: bool
        """
        