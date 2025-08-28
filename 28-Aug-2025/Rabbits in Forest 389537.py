# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        count = Counter(answers)
        sum = 0
        for freq, numOfRab in count.items():
            #NumberofGroupsNeeded * totalRabbits
            sum += ((freq+numOfRab)//(freq+1))*(freq+1)
        return sum
        """
        :type answers: List[int]
        :rtype: int
        """
        