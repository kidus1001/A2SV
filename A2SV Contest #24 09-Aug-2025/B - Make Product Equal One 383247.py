# Problem: B - Make Product Equal One - https://codeforces.com/gym/626626/problem/B

nums = int (input())
line = list(map(int, input().split()))

sum = 0

zero = 0
pos = 0
neg = 0

for i in range (nums):
     if (line[i]<0):
          sum += abs(1+line[i])
          neg+=1
     elif ((line[i]>0)) :
          sum += abs(line[i] - 1)
          pos+=1
     else:
          sum+=1
          zero+=1
     
if neg%2 == 1:
     if zero == 0:
          sum+=2

print (sum)