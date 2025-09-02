# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2
    
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(" ".join(map(str, arr)))
        i -= 1
    
    arr[i + 1] = value
    print(" ".join(map(str, arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
