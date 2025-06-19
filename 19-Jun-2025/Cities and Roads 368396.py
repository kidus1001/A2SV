# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

# example below, replace it with your solution
n = int(input())

graph = []

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

numberOfOnes = 0
for i in range(len(graph)):
    for j in range(i+1, len(graph[0])):
        if (graph[i][j]) == 1:
            numberOfOnes+=1
print(numberOfOnes)
