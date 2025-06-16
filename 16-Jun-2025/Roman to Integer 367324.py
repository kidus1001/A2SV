# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution(object):
    def romanToInt(self, s):
        res = 0
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        for i in range (len(s)-1):
            if (roman[s[i]] < roman[s[i+1]]):
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        res += roman[s[len(s)-1]]
        return res
        """
        :type s: str
        :rtype: int
        """
        