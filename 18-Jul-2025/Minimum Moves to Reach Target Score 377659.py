# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution(object):
    def minMoves(self, target, maxDoubles):
        answer = 0
        while target > 1 and maxDoubles > 0:
            if target%2 == 0:
                target //= 2
                maxDoubles-=1
            else:
                target -=1
            answer+=1
        answer += target
        return answer-1


        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        