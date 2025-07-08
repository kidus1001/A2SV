# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution(object):
    def findKthLargest(self, nums, k):

        import heapq
        return heapq.nlargest(k, nums)[-1]







        # import heapq
        # heapq.heapify(nums)
        
        # sortedList = []
        
        # while nums:
        #     sortedList.append(heapq.heappop(nums))
        
        # pos = len(nums) - 1 - k
        # return nums[pos]

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        