# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted (nums1+nums2)
        if (len(merged) %2 == 1):
            return merged [len(merged)/2]
        else:
            pos1 = (len(merged) - 2)/2
            pos2 = len(merged) / 2
            mid = (merged[pos1] + merged[pos2])/2.0
            return mid
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        