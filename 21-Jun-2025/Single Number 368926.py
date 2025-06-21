# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        num  = 0
        for i in range(len(nums)):
            num = num ^ nums[i]
        return num
        """
        :type nums: List[int]
        :rtype: int
        """
        