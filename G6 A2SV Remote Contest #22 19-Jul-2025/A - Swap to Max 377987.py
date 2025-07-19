# Problem: A - Swap to Max - https://codeforces.com/gym/622136/problem/A

testCases = int(input())
for _ in range(testCases):
     n = int(input())
     arr1 = list(map(int, input().split()))
     arr2 = list(map(int, input().split()))
     for i in range (n):
          if (arr1[i]>arr2[i]):
               arr1[i], arr2[i] = arr2[i], arr1[i]
     
     num1 = max(arr1)
     num2 = max(arr2)
     
     print(num1*num2)