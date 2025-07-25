# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies, k):
        self.ans = float('inf')  # best unfairness found so far
        distribution = [0] * k   # cookies each child has
        
        def backtrack(index):
            if index == len(cookies):  # all cookie bags are distributed
                self.ans = min(self.ans, max(distribution))  # update result
                return
            
            seen = set()  # for symmetry pruning
            
            for i in range(k):  # try giving cookies[index] to each child
                if distribution[i] in seen:
                    continue  # skip same state
                
                seen.add(distribution[i])
                
                distribution[i] += cookies[index]  # assign to child i
                # only proceed if current max is better than best so far
                if max(distribution) < self.ans:
                    backtrack(index + 1)
                distribution[i] -= cookies[index]  # backtrack

        backtrack(0)
        return self.ans
