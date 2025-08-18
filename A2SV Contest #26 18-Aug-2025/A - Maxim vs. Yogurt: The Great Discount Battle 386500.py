# Problem: A - Maxim vs. Yogurt: The Great Discount Battle - https://codeforces.com/gym/629689/problem/A

testCases = int(input())
for _ in range(testCases):
     n, priceOne, promotional = map(int, input().split())
     if ((promotional/2.0) > priceOne):
          print (n*priceOne)
     else:
          if (n%2 == 0):
               print (n//2 * promotional)
          else:
               print ((n//2 * promotional) + priceOne)