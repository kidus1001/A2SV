# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution(object):
    def hammingDistance(self, x, y):
        xor = str(bin(x^y))
        return xor.count('1')