# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        number = 0
        for i in digits:
            number = number * 10 + i
        newNum = number+1

        numberArray = []

        while newNum > 0:
            rem = newNum % 10
            newNum /= 10
            numberArray.append(rem)
        
        numberArray.reverse()

        return numberArray
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        