# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution(object):
    def decode(self, encoded):
        mod = ((len(encoded)+1)%4)
        x = 0
        if mod == 0:
            x = len(encoded)+1
        elif mod == 1:
            x = 1
        elif mod == 2:
            x = len(encoded)+2
        else:
            x = 0

        halfX = 0
        counter = 1
        while counter <= len(encoded):
            halfX ^= encoded[counter]
            counter+=2
        firstIndex = x ^ halfX
        print (firstIndex)

        answer = []
        answer.append(firstIndex)

        for i in range(1, len(encoded)+1):
            answer.append(answer[i-1] ^ encoded[i-1])
        return answer

        
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        