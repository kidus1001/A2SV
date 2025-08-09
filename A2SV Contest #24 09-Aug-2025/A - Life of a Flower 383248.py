# Problem: A - Life of a Flower - https://codeforces.com/gym/626626/problem/A

testCases = int(input())
for _ in range(testCases):
     initialHeight = 1
     size = int(input())
     line = list(map(int, input().split()))
     
     for i in range (size):

          if line[i] == 1:
               initialHeight += 1
               if i>0 and line[i-1]==1:
                    initialHeight += 4
          elif i>0 and line[i] == 0 and line[i-1] == 0:
               initialHeight =-1
               break
               
               
          
          
          
     print(initialHeight)