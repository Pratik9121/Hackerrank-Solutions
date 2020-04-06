#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mi = scores[0]
    mx = scores[0]
    cl = 0
    ch = 0
    l = []
    for i in range(1,len(scores)):
        if(scores[i] > mx):
            mx = scores[i]
            ch += 1
        elif(scores[i] < mi):
            mi = scores[i]
            cl += 1
    l.append(ch)
    l.append(cl)
    return l 
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
