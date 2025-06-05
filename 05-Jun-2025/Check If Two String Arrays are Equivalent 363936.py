# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        string1 = ""
        string2 = ""
        for x in word1:
            string1 += x
        for x in word2:
            string2 += x
        if (string1 == string2):
            return True
        else:
            return False
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        