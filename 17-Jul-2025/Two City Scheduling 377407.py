# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution(object):
    def twoCitySchedCost(self, costs):
        n = len(costs)
        costs.sort(key=lambda x: x[0] - x[1])
        
        
        answer = 0
        for i in range(n//2):
            answer += costs[i][0]
        for i in range(n//2, n):
            answer += costs[i][1]
        return answer
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        