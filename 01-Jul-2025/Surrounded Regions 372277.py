# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution(object):
    def solve(self, board):
        r = len(board)
        c = len(board[0])

        visited = [[False] * c for _ in range (r)]

        def dfs (i, j):
            if (i < 0 or j < 0 or i == r or j == c or board[i][j] != 'O'):
                return
            board[i][j] = 'K'
            dfs (i+1, j)
            dfs (i-1, j)
            dfs (i, j+1)
            dfs (i, j-1)

        for i in range (r):
            for j in range (c):
                if (board[i][j] == 'O' and (i in [0, r-1] or j in [0, c-1])):
                    dfs(i,j)

        for i in range (r):
            for j in range (c):
                if (board[i][j] == 'O'):
                    board[i][j] = 'X'
                elif (board[i][j] == 'K'):
                    board[i][j] = 'O'
        





        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        