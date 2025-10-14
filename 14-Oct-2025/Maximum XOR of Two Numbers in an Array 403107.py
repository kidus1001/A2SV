# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask = 0
        max_xor = 0
        for i in range(32, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            candidate = max_xor | (1 << i)
            for prefix in prefixes:
                if prefix ^ candidate in prefixes:
                    max_xor |= candidate
                    break

        return max_xor