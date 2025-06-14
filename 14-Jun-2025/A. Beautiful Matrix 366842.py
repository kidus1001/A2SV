# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

x = 0
y = 0

matrix = []
for i in range(5):
     line = list(map(int, input().split()))
     matrix.append(line)
     
for i in range(5):
     for j in range(5):
          if (matrix[i][j] == 1):
               x = i
               y = j
result = abs(x-2) + abs(y-2)
print (result)