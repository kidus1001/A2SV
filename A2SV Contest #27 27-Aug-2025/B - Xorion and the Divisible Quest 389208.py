# Problem: B - Xorion and the Divisible Quest - https://codeforces.com/gym/630556/problem/B

n = int(input())
listGiven = list(map(int, input().split()))
answer = min(listGiven)
check = True
for i in listGiven:
     if i%answer!=0:
          check=False
          break
if (check):
     print (answer)
else:
     print(-1)