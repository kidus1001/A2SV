# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
    def findWords(self, words):
        firstRow = ['q','w','e','r','t','y','u','i','o','p']
        secondRow = ['a','s','d','f','g','h','j','k','l']
        thirdRow = ['z','x','c','v','b','n','m']
        result = []
        for word in words:
            bool1 = True
            bool2 = True
            bool3 = True
            word1 = word.lower()
            for x in word1:
                if (x not in firstRow):
                    bool1 = False
                    break
            for x in word1:
                if (x not in secondRow):
                    bool2 = False
                    break
            for x in word1:
                if (x not in thirdRow):
                    bool3 = False
                    break
            if (bool1 or bool2 or bool3):
                result.append(word)
        
        return result




        """
        :type words: List[str]
        :rtype: List[str]
        """
        