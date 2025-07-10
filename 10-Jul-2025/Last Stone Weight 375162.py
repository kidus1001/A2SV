# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while (len(stones)>1):
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if (two > one):
                heapq.heappush(stones, one - two)
        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])
        
        """
        :type stones: List[int]
        :rtype: int
        """
        