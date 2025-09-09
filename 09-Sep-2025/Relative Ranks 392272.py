# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution(object):
    def findRelativeRanks(self, score):
        newList = []
        for i in range(len(score)):
            num = score[i]
            count = 1
            for j in range(len(score)):
                if(i == j):
                    continue
                else:
                    if(score[j] > score[i]):
                        count+=1
            if (count == 1):
                newList.append("Gold Medal")
            elif (count == 2):
                newList.append("Silver Medal")
            elif (count == 3):
                newList.append("Bronze Medal")
            else:
                newList.append(str(count))
        return newList
        """
        :type score: List[int]
        :rtype: List[str]
        """
        