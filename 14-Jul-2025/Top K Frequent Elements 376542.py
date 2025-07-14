# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution(object):
    def topKFrequent(self, nums, k):
        heap = []
        count = collections.Counter(nums)
        
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        