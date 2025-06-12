# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

# example below, replace it with your solution
n = int(input())
adj_matrix = []

for x in range(n):
    line = list(map(int, input().split()))
    adj_matrix.append(line)

count = 0
for i in range (n):
    for j in range (n):
        if adj_matrix[i][j] == 1:
            count+=1
print(count//2)
