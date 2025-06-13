# Problem: Team - https://codeforces.com/contest/231/problem/A

n =int(input())

total = 0
for problem in range(n):
     numLine = list(map(int, input().split(' ')))
     count=0
     for x in numLine:
          if x == 1:
               count+=1
     if (count >= 2):
          total+=1
print (total)