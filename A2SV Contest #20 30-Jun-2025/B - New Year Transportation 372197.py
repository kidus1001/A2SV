# Problem: B - New Year Transportation - https://codeforces.com/gym/618729/problem/B

n, destination = map(int, input().split())
 
line = list(map(int, input().split()))
 
line.insert(0, 0)
 
i = 1
 
while (i <= destination):
     if (i == destination):
          print ("YES")
          break
     i += line[i]
     
     if (i > destination):
          print("NO")
          break