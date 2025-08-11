# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution(object):
    def isAdditiveNumber(self, num):
        def check(a0, a1, num):
            i = 0
            while i < len(num):
                a0 = int(a0)
                a1 = int(a1)

                res = str(a0 + a1)
                j = 0

                while i < len(num) and j < len(res) and res[j] == num[i]:
                    j, i = j + 1, i + 1
                if j < len(res):
                    return False
                a0, a1 = a1, res

            return True

        def invalid(x):
            return x[0] == '0' and len(x) > 1

        n = len(num)

        for j in range(1, n - 1):
            for i in range(0, j):
                a0 = num[:i + 1]
                a1 = num[i + 1:j + 1]

                if invalid(a0) or invalid(a1):
                    continue

                if check(a0, a1, num[j + 1:]):
                    return True

        return False

        """
        :type num: str
        :rtype: bool
        """
        