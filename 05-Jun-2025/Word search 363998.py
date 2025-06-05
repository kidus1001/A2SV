# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs (r, c, i): #row, column (Meaning which cell we are in) + i (the position of the word)
            if (i == len(word)):
                return True #Meaning that the word is there boom!
            if (r<0 or c <0 or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in path): #Means we have already been there)
                return False
            path.add((r,c))
            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r, c-1, i+1) #down, up, right, left
            path.remove((r,c))
            return res

        for r in range(rows):
            for c in range (cols):
                if (dfs(r,c,0)):
                    return True
        return False

        
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        