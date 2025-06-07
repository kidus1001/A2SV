# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    
    def merge(self, nums1, m, nums2, n):
        nums1Copy = []
        for x in range(m):
            nums1Copy.append(nums1[x])
        mergedList = sorted(nums1Copy+nums2)
        for i in range(m+n):
            nums1[i] = mergedList[i]
        return nums1
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        