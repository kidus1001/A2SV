# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        potential = []
        results = []
        def backTrack (i, cur_sum):
            if (cur_sum == target):
                results.append(list(potential))
                return
            if (cur_sum > target):
                return

            for x in range(i, len(candidates)):
                potential.append(candidates[x])
                backTrack(x, cur_sum+candidates[x])
                potential.pop()
        backTrack (0, 0)
        return results

        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        