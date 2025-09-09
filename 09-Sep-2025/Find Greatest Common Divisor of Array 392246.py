# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

import math
class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        mn = nums[0]
        mx = nums[len(nums)-1]

        answer = 1
        for i in range (2, mn+1):
            if (mn%i == 0 and mx%i == 0):
                answer = i
        return answer
        """
        :type nums: List[int]
        :rtype: int
        """
        