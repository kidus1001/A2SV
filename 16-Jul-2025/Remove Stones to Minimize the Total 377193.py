# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution(object):
    def minStoneSum(self, piles, k):
        heap = []
        maxHeap = [-num for num in piles]
        heapq.heapify(maxHeap)
        for i in range(0, k):
            num = -1 * heapq.heappop(maxHeap)
            numToAdd = num - (num//2)
            heapq.heappush(maxHeap, -numToAdd)
        sum = 0
        for i in range (len(maxHeap)):
            sum += -1 * maxHeap[i]
        return sum
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        