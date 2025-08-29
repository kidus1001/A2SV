# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution(object):
    def equationsPossible(self, equations):
        parent = [i for i in range(26)]

        def find (x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]

        def union (a, b):
            ua = find(a)
            ub = find(b)

            parent[ua] = ub

        for e in equations:
            if (e[1] == "!"):
                continue
            a = ord(e[0]) - ord('a')
            b = ord(e[3]) - ord('a')

            union(a,b) 

        for e in equations:
            if (e[1] == "="):
                continue
            a = ord(e[0]) - ord('a')
            b = ord(e[3]) - ord('a')

            if (find(a) == find(b)):
                return False
        return True
        

        """
        :type equations: List[str]
        :rtype: bool
        """
        