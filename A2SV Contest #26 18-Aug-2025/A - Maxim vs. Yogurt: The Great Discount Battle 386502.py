# Problem: A - Maxim vs. Yogurt: The Great Discount Battle - https://codeforces.com/gym/629689/problem/A

testCases = int(input())
for _ in range(testCases):
     n, priceOne, promotional = map(int, input().split())
     
     costNormal = n*priceOne
     costPromo = ((n//2) * promotional) + (n%2) * priceOne
     print (min(costNormal, costPromo))