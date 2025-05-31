# Problem: Find Target Indices After Sorting Indices - https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        lists = []
        i = 0
        j = 0
        for x in nums:
            if (x == target):
                lists.append(i)
                j+=1
            i+=1
        return lists

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """