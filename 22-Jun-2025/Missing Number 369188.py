# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        for num in range(len(nums)):
            if num not in nums:
                return num
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        