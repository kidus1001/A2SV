# Problem: A - Card Game - https://codeforces.com/gym/616066/problem/A

n = int(input())

for _ in range(n):
     line = list(map(int, input().split()))
     
     line1 = list(map(int, input().split()))
     line2 = list(map(int, input().split()))
     
     if max(line1) > max(line2):
          print("YES")
     else:
          print("NO")