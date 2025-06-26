# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for i in letters:
            if i > target:
                return i
        return letters[0]
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        