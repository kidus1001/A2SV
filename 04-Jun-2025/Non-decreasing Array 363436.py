# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution(object):
    def checkPossibility(self, nums):
        changed = False
        for i in range(len(nums)-1):
            if (nums[i] <= nums[i+1]):
                continue
            if changed:
                return False
            if (i==0 or nums[i+1] >= nums[i-1]):
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed = True
        return True

        """
        :type nums: List[int]
        :rtype: bool
        """
        