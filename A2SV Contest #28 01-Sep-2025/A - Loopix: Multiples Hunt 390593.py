# Problem: A - Loopix: Multiples Hunt - https://codeforces.com/gym/632067/problem/A

import math
testCases = int(input())
for _ in range(testCases):
     l, r, k = map(int, input().split())
     i = (r+1)/k
     k = math.ceil(i)
     if (k<l):
          print (0)
     else:
          print(k-l)
