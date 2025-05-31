# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        i = 0
        while (i < len(nums)-1):
            if (nums[i] == nums[i+1]):
                nums.pop(i+1)
            else:
                i+=1

        if (len(nums) <3):
            return nums[len(nums)-1]
        else:
            return nums[len(nums)-3]
        """
        :type nums: List[int]
        :rtype: int
        """
        