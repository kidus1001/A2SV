# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        min_heap = []

        # Push the first element of each row into the heap
        for row in range(min(k, n)):
            heapq.heappush(min_heap, (matrix[row][0], row, 0))

        # Extract-min k times
        while k > 0:
            val, r, c = heapq.heappop(min_heap)
            k -= 1
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

        return val
