# Problem: Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/

class Solution(object):
    def getConcatenation(self, nums):
        for i in range (len(nums)):
            nums.append(nums[i])
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums