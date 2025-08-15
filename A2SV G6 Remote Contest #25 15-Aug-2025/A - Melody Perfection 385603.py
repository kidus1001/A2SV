# Problem: A - Melody Perfection - https://codeforces.com/gym/628023/problem/A

testCases = int(input())

for _ in range (testCases):
     perfectCheck = True
     size = int(input())
     melodies = list(map(int, input().split()))
     
     for i in range(len(melodies)-1):
          res = abs(melodies[i] - melodies[i+1])
          if not(res == 5 or res == 7):
               perfectCheck = False
               break
     if perfectCheck:
          print ("YES")
     else:
          print("NO")