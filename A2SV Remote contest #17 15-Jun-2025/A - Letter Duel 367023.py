# Problem: A - Letter Duel - https://codeforces.com/gym/614464/problem/A

n = int(input())

for problems in range(n):
     flag = True
     l = 0
     r = 0
     stringSize = int(input())
     myStringInput = input()
     for i in range(stringSize-1):
          if (myStringInput[i]!=myStringInput[i+1]):
               flag = False
               l = i+1
               r = i+2
     if (flag == False):
          print (l, r)
     else:
          print (-1,-1)