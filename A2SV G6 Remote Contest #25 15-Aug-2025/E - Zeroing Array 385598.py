# Problem: E - Zeroing Array - https://codeforces.com/gym/628023/problem/E

from sys import stdin

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

total = max_value = 0
for a in arr:
    total += a
    max_value = max(max_value, a)
    
if total % 2 == 1  or  max_value > total - max_value:
    print("NO")
else:
    print("YES")