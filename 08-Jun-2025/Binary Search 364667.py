# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution(object):
    def binarySearch (self, nums, target, left, right):
        if (left > right):
            return -1
        mid = (left+right)//2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] > target):
            return self.binarySearch(nums, target, left, mid-1)
        else:
            return self.binarySearch (nums, target, mid+1, right)
    
    def search(self, nums, target):
        return self.binarySearch (nums, target, 0, len(nums)-1)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        