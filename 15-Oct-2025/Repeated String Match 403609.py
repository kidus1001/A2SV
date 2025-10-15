# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        sub = len(b)//len(a)
        counter = 1
        while counter <= sub+2:
            if b in a*counter:
                return counter
            else:
                counter+=1
        return -1