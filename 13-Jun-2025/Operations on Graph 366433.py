# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

n = int(input())

graph = [[] for _ in range(n)]

numOfOperations = int(input())

for _ in range(numOfOperations):
    operation = list(map(int, input().split()))
    
    if operation[0] == 1:
        u, v = operation[1] - 1, operation[2] - 1
        graph[u].append(v)
        graph[v].append(u)

    elif operation[0] == 2:
        u = operation[1] - 1
        neighbors = graph[u]

        neighbors = [str(v + 1) for v in neighbors]
        print(' '.join(neighbors))
