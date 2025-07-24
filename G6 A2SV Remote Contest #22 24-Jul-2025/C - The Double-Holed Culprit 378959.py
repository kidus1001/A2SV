# Problem: C - The Double-Holed Culprit - https://codeforces.com/gym/622136/problem/C

n = int(input())
p = list(map(int, input().split()))

for a in range(n):
    visited = set()
    current = a
    while current not in visited:
        visited.add(current)
        current = p[current] - 1
    print(current + 1, end=' ')
