# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

import math

class Solution:
    def is_prime(self, x: int) -> bool:
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        r = int(math.isqrt(x))
        for i in range(3, r + 1, 2):
            if x % i == 0:
                return False
        return True

    def primePalindrome(self, n: int) -> int:
        # handle small cases directly
        if n <= 2: return 2
        if n <= 3: return 3
        if n <= 5: return 5
        if n <= 7: return 7
        if n <= 11: return 11

        # generate odd-length palindromes
        for length in range(1, 6):  # up to 10^8 (9 digits)
            start = 10**(length-1)
            end = 10**length
            for half in range(start, end):
                s = str(half)
                # make odd-length palindrome
                pal = int(s + s[-2::-1])
                if pal >= n and self.is_prime(pal):
                    return pal
        return -1
