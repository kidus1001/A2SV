# Problem: H - Grid 1 - https://atcoder.jp/contests/dp/tasks/dp_h

n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=list(input())
    mat.append(l)
dp=[[0]*m for i in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(m):
        if mat[i][j]=="#":
            dp[i][j]=0
        else:
            if i>0 and j>0:
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%(10**9+7)
            elif i>0:
                dp[i][j]=dp[i-1][j]%(10**9+7)
            elif j>0:
                dp[i][j]=dp[i][j-1]%(10**9+7)
print(dp[-1][-1])

            

