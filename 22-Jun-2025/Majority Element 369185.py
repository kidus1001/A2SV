# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if (count == 0):
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
        """
        :type nums: List[int]
        :rtype: int
        """
        