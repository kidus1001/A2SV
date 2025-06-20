# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

vertices = int(input())
graph = []
for i in range(vertices):
    line = []
    for j in range(vertices):
        line.append(0)
    graph.append(line)


for i in range(vertices):
    line = list(map(int, input().split()))
    n = line[0]
    for j in range(1, n+1):
        graph[i][line[j]-1] = 1

for i in range(len(graph)):
    print (*graph[i])
