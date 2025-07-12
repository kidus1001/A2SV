# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution(object):
    def buildArray(self, nums):
        res = []
        for i in nums:
            res.append(nums[i])
        return res
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        