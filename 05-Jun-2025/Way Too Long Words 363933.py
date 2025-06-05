# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n =int(input())

for words in range (n):
     word = input()
     if (len(word) > 10):
          size = len(word)-2
          firstCharacter = word[0]
          lastCharacter = word[len(word)-1]
          print(firstCharacter+str(size)+lastCharacter)
     else:
          print (word)
          