# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def dfs (i, cur, total):
            if sum (cur) == target:
                res.append(cur[:])
                return
            if total > target or i >= len(candidates):
                return

            total += candidates[i]
            cur.append(candidates[i])
            dfs (i, cur, total)
            cur.pop()

            dfs (i+1, cur, total - candidates[i])

        dfs(0, [], 0)
        return res

        


        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        