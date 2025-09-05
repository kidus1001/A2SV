# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        count = collections.Counter(nums)
        twice = [num for num, freq in count.items() if freq == 2]
        return twice
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        