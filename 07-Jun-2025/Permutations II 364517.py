# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution(object):
    def permuteUnique(self, nums):
        possibleCombination = []
        potential = []
        used = [False] * len(nums)
        nums.sort()

        def backTrack():
            if len(potential) == len(nums):
                possibleCombination.append(list(potential))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                potential.append(nums[i])
                backTrack()
                potential.pop()
                used[i] = False

        backTrack()
        return possibleCombination
