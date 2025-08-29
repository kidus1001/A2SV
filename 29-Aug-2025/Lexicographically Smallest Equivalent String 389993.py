# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        parent = list(range(26))

        def find (x):
            if (parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]

        def union (a, b):
            findX, findY = find(a), find(b)
            if (findX == findY):
                return
            elif (findX < findY):
                parent[findY] = findX
            else:
                parent[findX] = findY

        for a, b in zip(s1, s2):
            union (ord(a) - ord('a'), ord(b) - ord('a'))

        result = []
        for ch in baseStr:
            smallest = chr(find(ord(ch) - ord('a')) + ord('a'))
            result.append(smallest)

        return ''.join(result)        

        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        