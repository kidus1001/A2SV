# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
h = list(map(int, input().split()))

dp = [0]*n

for i in range(1,n):
  cost = dp[i-1]+abs(h[i]-h[i-1])
  if i > 1:
    cost2 = dp[i-2]+ abs(h[i]-h[i-2])
    dp[i] = min(cost,cost2)
  else:
    dp[i] = cost
print (dp[n-1])