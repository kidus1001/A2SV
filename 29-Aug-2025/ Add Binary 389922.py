# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        aRev = a[::-1]
        bRev = b[::-1]

        answer = ""
        minNum = min (len(a), len(b))

        carry = 0
        for i in range(minNum):
            sum = int(aRev[i]) + int(bRev[i]) + carry

            if sum == 3:
                sum = 1
                carry = 1
            elif sum == 2:
                sum = 0
                carry = 1
            elif sum == 1:
                carry = 0
                sum = 1
            else:
                carry = 0
                sum = 0
            answer += str(sum)

        for j in range (minNum, max(len(a), len(b))):
            if (len(a) > len(b)):
                sum = int(aRev[j]) + carry
            else:
                sum = int(bRev[j]) + carry

            if sum == 3:
                sum = 1
                carry = 1
            elif sum == 2:
                sum = 0
                carry = 1
            elif sum == 1:
                carry = 0
                sum = 1
            else:
                carry = 0
                sum = 0
            answer += str(sum)
        if carry:
            answer += str(carry)
        return answer[::-1]
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        