# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def frog_min_cost(h, K):
    n = len(h) - 1  # assuming h[1..N]
    INF = 10**18
    dp = [INF] * (n + 1)
    dp[1] = 0
    for i in range(2, n + 1):
        for j in range(1, min(K, i - 1) + 1):
            dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))
    return dp[n]
