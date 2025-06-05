# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution(object): #Neetcode
    def restoreIpAddresses(self, s):
        res = []
        if (len(s) > 12):
            return res
        def backTrack (i, dots, currentIP):
            #Base cases
            if (dots == 4 and i == len(s)):  
                res.append(currentIP[:-1]) #Removing the last dot on our IP
                return
            if (dots > 4):
                return
            for j in range(i, min((i+3), len(s))):
                if ( int((s[i:j+1])) <= 255 and (i==j or s[i]!="0")):
                    backTrack (j+1, dots+1, currentIP + s[i:j+1] + ".")
        backTrack (0,0,"")
        return res

        """
        :type s: str
        :rtype: List[str]
        """
        