# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution(object):
    def maximumGap(self, nums):
        if (len(nums)<2):
            return 0
        nums.sort()
        maximum = 0
        for i in range(1, len(nums)):
            maximum = max(maximum, nums[i]-nums[i-1])
        return maximum
        """
        :type nums: List[int]
        :rtype: int
        """
        