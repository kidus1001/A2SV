# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

import sys
input = sys.stdin.readline

def v2(x):
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = sum(v2(x) for x in a)
    
    if total >= n:
        print(0)
        continue
    
    need = n - total
    gains = []
    
    for i in range(1, n + 1):
        gains.append(v2(i))
    
    gains.sort(reverse=True)
    
    added = 0
    used = 0
    for g in gains:
        if g == 0:
            break
        added += g
        used += 1
        if added >= need:
            break
    
    if added >= need:
        print(used)
    else:
        print(-1)
