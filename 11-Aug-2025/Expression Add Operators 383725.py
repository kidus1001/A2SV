# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution(object):
    def addOperators(self, num, target):
        def backtrack(i, path, resultSoFar, prevNum):
            if i == len(s):
                if resultSoFar == target:
                    ans.append(path)
                return

            for j in range(i, len(s)):
                if j > i and s[i] == '0':  # skip leading zeros
                    break
                curr = int(s[i:j + 1])
                if i == 0:
                    backtrack(j + 1, path + str(curr), curr, curr)
                else:
                    backtrack(j + 1, path + "+" + str(curr), resultSoFar + curr, curr)
                    backtrack(j + 1, path + "-" + str(curr), resultSoFar - curr, -curr)
                    backtrack(j + 1, path + "*" + str(curr), resultSoFar - prevNum + prevNum * curr, prevNum * curr)

        s = num
        ans = []
        backtrack(0, "", 0, 0)
        return ans
