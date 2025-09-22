# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input()) 

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()  
    
    flag = True
    for i in range(n - 1):
        if a[i+1] - a[i] > 1: 
            flag = False
            break
    
    if flag:
        print("yes")
    else:
        print("no")