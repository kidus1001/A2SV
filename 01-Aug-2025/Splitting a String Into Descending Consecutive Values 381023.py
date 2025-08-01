# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution(object):
    def splitString(self, s):
        def solve(s, i, length, prev, splits):
            if i == len(s) and splits >= 2: 
                return True
            while i + length <= len(s):
                cur = int(s[i:i+length])
                length += 1
                
                if prev != -1 and cur != prev - 1: continue 
                
                if solve(s, i + length - 1, 1, cur, splits + 1):
                    return True
            return False
        return solve(s, 0, 1, -1, 0)
        """
        :type s: str
        :rtype: bool
        """
        