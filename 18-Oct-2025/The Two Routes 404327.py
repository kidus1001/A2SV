# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque

V, E = map(int, input().split(" "))

railway = [[0] * (V + 1) for _ in range(V + 1)]
roads = [[1] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    railway[u][v] = 1
    railway[v][u] = 1
    roads[v][u] = 0
    roads[u][v] = 0

for i in range(1, V + 1):
    roads[i][i] = 0

def bfs01(graph):
    queue = deque([1])
    visited = {1}
    times = [float('inf')] * (V + 1)
    times[1] = 0

    while queue:
        u = queue.popleft()
        for v in range(1, V + 1):
            if graph[u][v] == 1 and v not in visited:
                visited.add(v)
                times[v] = times[u] + 1
                queue.append(v)
    return times[V] if times[V] != float('inf') else -1


railway_time = bfs01(railway)
roads_time = bfs01(roads)

if railway_time == -1 or roads_time == -1:
    print(-1)
else:
    print(max(railway_time, roads_time))