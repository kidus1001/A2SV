# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0]!=5:
            return False
        fiveDBills = 0
        tenDBills = 0
        for b in bills:
            if b == 5: fiveDBills+=1
            elif b == 10: 
                if fiveDBills > 0:
                   fiveDBills-=1
                else:
                    return False 
                tenDBills+=1
            else:
                if fiveDBills>0 and tenDBills > 0:
                    fiveDBills-=1
                    tenDBills-=1
                elif fiveDBills>2:
                    fiveDBills-=3
                else:
                    return False
        return True
        """
        :type bills: List[int]
        :rtype: bool
        """
        