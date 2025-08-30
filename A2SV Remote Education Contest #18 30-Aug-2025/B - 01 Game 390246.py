# Problem: B - 01 Game - https://codeforces.com/gym/616066/problem/B

n = int(input())

for _ in range (n):
     binaryInput = input()
     zeroCount = 0
     oneCount = 0
     for ch in range(len(binaryInput)):
          if binaryInput[ch] == '0':
               zeroCount+=1
          else:
               oneCount+=1
     pairs = 0
     if (zeroCount > oneCount):
          pairs = oneCount
     else:
          pairs = zeroCount
     
     if (pairs % 2 == 0):
          print("NET")
     else:
          print("DA")
          