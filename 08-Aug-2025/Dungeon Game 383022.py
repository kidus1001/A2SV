# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
        
        return dp[0][0]

        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        