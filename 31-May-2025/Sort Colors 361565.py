# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        r = 0
        w = 0
        b = 0
        for x in nums:
            if (x == 0):
                r+=1
            elif (x == 1):
                w+=1
            else:
                b+=1
        counter = 0
        while (r > 0):
            nums[counter] = 0
            r-=1
            counter+=1
        while (w > 0):
            nums[counter] = 1
            w-=1
            counter+=1
        while (b > 0):
            nums[counter] = 2
            b -= 1
            counter+=1

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        