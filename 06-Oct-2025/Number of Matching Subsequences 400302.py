# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution(object):
    def numMatchingSubseq(self, s, words):
        if not words or not s:
            return 0
        cache= {}
        answer = 0
        for i in words:
            if self.isSub(s, i, cache):
                answer += 1
        return answer

    def isSub (self, s, i, cache):
        if len (i) > len(s):
            return False
        k = 0
        for j in range(len(s)):
            if i[k] == s[j]:
                k+=1
                if k == len(i):
                    cache[i] = True
                    return True
        
        return False
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        