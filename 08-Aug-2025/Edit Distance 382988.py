# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:

#         row, col = len(word1), len(word2)
#         # dp[i][j] = edit distance between first i chars of word1 and first j chars of word2
#         dp = [[0] * (col + 1) for _ in range(row + 1)]

#         # case 1: what if word one was empty?
#         # -> insert every character in word2 
#         # the following just represents that case 
#         for j in range(col + 1):
#             dp[0][j] = j  # j insertions needed


#         # Fill the DP table
#         for i in range(1, row + 1):
#             dp[i][0] = i    # i deleations needed
#             for j in range(1, col + 1):
#                 if word1[i - 1] == word2[j - 1]:
#                     # Characters match, no operation needed
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = 1 + min(
#                         dp[i - 1][j],     # dp[i-1][j]   -> delete from word1
#                         dp[i][j - 1],     # dp[i][j-1]   -> insert into word1
#                         dp[i - 1][j - 1]  # dp[i-1][j-1] -> replace in word1
#                     )

#         return dp[row][col]









class Solution(object):
    def minDistance(self, word1, word2):
        memo = {}
        def helper (one, two):
            if (one, two) in memo:
                return memo[(one, two)]
            if one == 0:
                return two
            if two == 0:
                return one
            if word1[one-1] == word2[two-1]:
                memo[(one, two)] = helper(one-1, two-1)
                return memo[(one, two)]
            delete = helper(one-1, two)+1
            replace = helper (one-1, two-1)+1
            insert = helper(one, two-1)+1

            memo[(one, two)] = min(delete, replace, insert)
            return memo[(one, two)]
        
        return helper (len(word1), len(word2))
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
        