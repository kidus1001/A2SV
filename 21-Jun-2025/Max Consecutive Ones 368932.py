# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxOne = 0
        one = 0
        for i in range(len(nums)):
            if (nums[i] == 1):
                one+=1
            else:
                maxOne = max(maxOne, one)
                one = 0
        maxOne = max(maxOne, one)
        return maxOne
        """
        :type nums: List[int]
        :rtype: int
        """
        