# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        state = [0]*len(words)
        for i in range (len(words)):
            mask = 0
            for c in words[i]:
                mask |= 1<< (ord(c) - ord('a'))
            state[i] = mask

        n = len(words)
        max_prod = 0
        for i in range(n):
            for j in range(i + 1, n):
                if state[i] & state[j] == 0:
                    product = len(words[i]) * len(words[j])
                    max_prod = max(max_prod, product)
        return max_prod
                
        """
        :type words: List[str]
        :rtype: int
        """
        