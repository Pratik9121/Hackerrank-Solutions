#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    a = []
    s = 0
    for values in Counter(ar).values():
        a.append(values)
    for i in range(len(a)):
        if(a[i] > 0 and a[i] % 2 == 0):
            s += a[i] // 2
        else:
            a[i] -= 1
            s += a[i] // 2
    return s    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
