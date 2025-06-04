# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
    def findWords(self, words):
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        result = []
        for word in words:
            lower_word = set(word.lower())
            if (lower_word <= firstRow or lower_word <= secondRow or lower_word <= thirdRow):
                result.append(word)
        return result




        """
        :type words: List[str]
        :rtype: List[str]
        """
        