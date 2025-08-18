# Problem: B - Maxim vs. Letters: Newspaper Heist - https://codeforces.com/gym/629689/problem/B

from collections import Counter

s1 = input().rstrip('\n')
s2 = input().rstrip('\n')

cnt1 = Counter(ch for ch in s1 if ch != ' ')
cnt2 = Counter(ch for ch in s2 if ch != ' ')

for ch in cnt2:
    if cnt2[ch] > cnt1[ch]:
        print("NO")
        break
else:
    print("YES")
