# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution(object):
    def countPrimes(self, n):
        primes = [True] * (n+1)
        if n == 0:
            primes[0] = False
        else:
            primes[0] = primes[1] = False


        for i in range (2, int(n**0.5)+1):
            if primes[i]:
                for j in range (i*i, n+1, i):
                    primes[j] = False
        
        count = 0
        for i in range(len(primes)-1):
            if primes[i] == True:
                count += 1
        return count
        """
        :type n: int
        :rtype: int
        """
        