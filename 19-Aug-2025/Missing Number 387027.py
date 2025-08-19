# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        sumNums = sum(nums) #4
        n = len(nums) #3
        actualSum = (n * (n+1))//2 #12/2 = 6
        return actualSum-sumNums  #6-4
        """
        :type nums: List[int]
        :rtype: int
        """
        