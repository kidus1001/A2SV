# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
cnt = [0] * (n + 1)

for p in range(2, n + 1):
    if cnt[p] == 0:  # p is prime
        for k in range(p, n + 1, p):
            cnt[k] += 1  # count distinct prime factor

ans = sum(1 for i in range(1, n + 1) if cnt[i] == 2)
print(ans)
