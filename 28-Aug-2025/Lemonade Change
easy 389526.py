# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution(object):
    def lemonadeChange(self, bills):
        count5 = 0
        count10 = 0
        count20 = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                count5 += 1
            elif bills[i] == 10:
                count10 += 1
                if count5 > 0:
                    count5 -= 1 
                else:
                    return False 
            else:
                count20 += 1
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count5 -= 3
                else:
                    return False
        return True
