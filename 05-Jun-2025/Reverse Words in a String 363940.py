# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution(object):
    def reverseWords(self, s):
        string = s.split()
        newString = ""
        for x in range(len(string)-1, -1, -1):
            newString += string[x] + " "
        return (newString.strip())

        """
        :type s: str
        :rtype: str
        """
        