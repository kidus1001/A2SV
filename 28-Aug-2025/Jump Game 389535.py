# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums) - 1:
                return True
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """
        