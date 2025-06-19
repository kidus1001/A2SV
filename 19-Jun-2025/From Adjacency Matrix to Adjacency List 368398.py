# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())

graph = []
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

from collections import defaultdict
newGraph = defaultdict(list)

for i in range (n):
    for j in range (n):
        if graph[i][j] == 1:
            newGraph[i+1].append(j+1)

for i in range (1, n+1):
    print (len(newGraph[i]), *newGraph[i])