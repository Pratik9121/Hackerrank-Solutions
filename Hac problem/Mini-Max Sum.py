#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mi = min(arr)
    ma = max(arr)
    s1 , s2 = 0,0
    for i in range(len(arr)):
        s1 = sum(arr)-mi
        s2 = sum(arr)-ma
    print(s2,s1)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
