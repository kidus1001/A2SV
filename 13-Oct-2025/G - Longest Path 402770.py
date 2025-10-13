# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

n, edges = map(int, input().split())
h = defaultdict(list)
count = defaultdict(lambda: [0, 0])  # ingoing, outgoing

for _ in range(edges):
    start, end = map(int, input().split())
    h[start].append(end)
    count[start][1] += 1
    count[end][0] += 1

memo = {}
def dfs(node):
    if node in memo:
        return memo[node]
    best = 0
    for nxt in h[node]:
        best = max(best, 1 + dfs(nxt))
    memo[node] = best
    return best

ans = 0
for node in range(1, n+1):   
    ans = max(ans, dfs(node))
print(ans)