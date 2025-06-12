# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

vertices = int(input())
adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

for y in range (vertices):
    line = list(map(int, input().split()))
    size = line[0]
    for x in range(1, size+1):
        adj_matrix[y][line[x]-1] = 1

for row in adj_matrix:
    print (*row)

