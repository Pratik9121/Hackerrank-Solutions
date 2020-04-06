#!/bin/python3\
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    length = len(arr)
    for i in range(len(arr)):
        if(arr[i] < 0):
            neg += 1
        elif(arr[i] > 0):
            pos += 1
        else:
            zer += 1
    print(pos/length)
    print(neg/length)
    print(zer/length)        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
