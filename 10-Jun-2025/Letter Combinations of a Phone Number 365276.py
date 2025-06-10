# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        result = []
        digitsMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backTrack (i, potentialString):
            if (i == len(digits)):
                result.append(potentialString)
                return
            for x in digitsMap[digits[i]]:
                backTrack (i+1, potentialString+x)
        
        backTrack(0, "")
        if digits:
            return result
        else:
            return []
        """
        :type digits: str
        :rtype: List[str]
        """
        