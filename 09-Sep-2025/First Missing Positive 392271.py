# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution(object):
    def firstMissingPositive(self, nums):
        setNums = set(nums)
        i = 1
        while True:
            if i not in setNums:
                return i
            i+=1
        """
        :type nums: List[int]
        :rtype: int
        """
        