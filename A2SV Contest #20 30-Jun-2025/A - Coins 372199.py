# Problem: A - Coins - https://codeforces.com/gym/618729/problem/A

n = int(input())

for _ in range(n):
     a, b = map(int, input().split())
     if b%2 == 0 and a % 2 != 0:
          print ("NO")
     else:
          print("YES")
          