# Problem: B - Lifeboat Lineup - https://codeforces.com/gym/622136/problem/B

n = int (input())
lineOrder = []
lineName = []
lineAnswer = []
for _ in range(n):
     lineInput = list(map(str, input().split()))
     lineName.append(lineInput[0])
     if (lineInput[1] == 'captain'):
          lineOrder.append(4)
     elif lineInput[1] == 'man':
          lineOrder.append(3)
     elif lineInput[1] == 'woman' or lineInput[1] == 'child':
          lineOrder.append(2)
     else:
          lineOrder.append(1)
          print(lineInput[0])
          
for i in range(n):
     if lineOrder[i] == 2:
          lineAnswer.append(lineName[i])
          print(lineName[i])
          
for i in range(n):
     if lineOrder[i] == 3:
          lineAnswer.append(lineName[i])
          print(lineName[i])
          
for i in range(n):
     if lineOrder[i] == 4:
          lineAnswer.append(lineName[i])
          print(lineName[i])
