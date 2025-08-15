# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution(object):
    def knightProbability(self, n, k, row, col):
        cache = {}

        def dfs(k, row, col):
            if row < 0 or row >= n or col < 0 or col >= n:
                return 0.0
            if k == 0:
                return 1.0

            state = (k, row, col)
            if state in cache:
                return cache[state]

            nextMoves = [
                (row - 2, col - 1), (row - 2, col + 1),
                (row + 2, col - 1), (row + 2, col + 1),
                (row - 1, col - 2), (row - 1, col + 2),
                (row + 1, col - 2), (row + 1, col + 2)
            ]

            prob = 0.0
            for nextRow, nextCol in nextMoves:
                prob += (1 / 8.0) * dfs(k - 1, nextRow, nextCol)

            cache[state] = prob
            return prob

        return dfs(k, row, col)
