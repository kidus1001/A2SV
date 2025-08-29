# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        subset = []
        for i in range (2**len(nums)):
            current = []
            for j in range (len(nums)):
                if i & (1 << j):
                    current.append(nums[j])
            subset.append(current)
        return subset
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        