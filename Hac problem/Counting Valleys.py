#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    l = list(s)
    count = 0
    c = 0
    for i in range(len(l)):
        if(l[i] == 'U'):
            count += 1
        if(l[i] == 'D'):
            count -= 1
        if(count == 0 and l[i] == 'U'):
            c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
