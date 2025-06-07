# Problem: Search Insert Position - https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        firstIndex = 0
        lastIndex = len(nums) -1
        mid = 0
        while (firstIndex<=lastIndex):
            mid = (firstIndex+lastIndex)//2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                lastIndex = mid-1
            else:
                firstIndex = mid+1
        return firstIndex
        

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        