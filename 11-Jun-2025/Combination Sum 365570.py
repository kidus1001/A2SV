# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        potentialList = []
        uniqueStorage = set()
        def backTrack (i, potentialList, sum):
            if (sum == target and tuple(potentialList) not in uniqueStorage):
                result.append(potentialList[:])
                uniqueStorage.add(tuple(potentialList))
                return
            elif (sum > target): 
                return
            for i in range(i,len(candidates)):
                potentialList.append(candidates[i])
                sum += candidates[i]
                backTrack(i, potentialList, sum)
                sum -= candidates[i]
                potentialList.pop()
            
        backTrack (0,[],0)
        return result
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        