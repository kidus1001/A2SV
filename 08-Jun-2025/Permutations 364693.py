# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        result = []

        def backTrack (trial):
            if (len(trial) == len(nums)):
                result.append(trial[:])
                return
            for i in range (len(nums)):
                if nums[i] not in trial:
                    trial.append(nums[i])
                    backTrack(trial)
                    trial.pop()

        backTrack([])
        return result
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        