# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for i in range (len(nums)-2):
            if (nums[i] < nums[i+1]+nums[i+2]):
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
        """
        :type nums: List[int]
        :rtype: int
        """
        