# Problem:  Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

class Solution(object):
    def findTheLongestSubstring(self, s):
        vowels = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        mask = 0
        seen = {0:-1}
        ans = 0

        for i, char in enumerate (s):
            if char in vowels:
                mask ^= (1 << vowels[char])
            if mask in seen:
                ans = max(ans, i-seen[mask])
            else:
                seen[mask] = i
        return ans