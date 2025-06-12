# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

# example below, replace it with your solution
vertices, edges = map(int, input().split(" "))
adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

for _ in range (edges):
    v1, v2 = map(int, input().split(" "))
    adj_matrix[v1-1][v2-1] = 1
    adj_matrix[v2-1][v1-1] = 1

degreeList = []
for i in range(vertices):
    degree = 0
    for j in range(vertices):
        if (adj_matrix[i][j] == 1):
            degree += 1
    degreeList.append(degree)

if all (d == degreeList[0] for d in degreeList):
    print("YES")
else:
    print ("NO")