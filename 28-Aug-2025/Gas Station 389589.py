# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        diff = []
        for i in range (len(gas)):
            diff.append(gas[i]-cost[i])
        if sum(gas) < sum(cost):
            return -1
        start = 0
        total = 0
        for i in range(len(diff)):
            total+=diff[i]
            if total < 0:
                total = 0
                start = i+1
        return start
        
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        