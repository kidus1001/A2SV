# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        row = len(board)
        col = len (board[0])
        path = set()
        def backTrack (r, c, i):
            if i == len(word)-1:
                return word[i] == board[r][c]
            if board[r][c] != word[i] or r<0 or c < 0 or r >= row or c >= col or (r,c) in path:
                return False
            path.add((r,c))
            directions = [(-1,0), (1,0), (0,1), (0,-1)]
            for x,y in directions:
                rowNew = r + x
                colNew = c+y
                if (0 <= rowNew < row and 0 <= colNew < col and (rowNew,colNew) not in path):
                    if backTrack (rowNew, colNew, i+1):
                        return True
            path.remove((r,c))
            return False
                    

            


        for x in range (row):
            for y in range (col):
                if board[x][y] == word[0] and backTrack (x,y,0):
                    return True
        return False

        
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        