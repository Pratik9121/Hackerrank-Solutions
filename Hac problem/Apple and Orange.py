#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count1 , count2 = 0 , 0
    s1 = 0
    s2 = 0
    for i  in range(len(apples)):
        s1 = 0 
        s1 = a + apples[i]
        if(s1 >= s and s1 <= t):
            count1 += 1
    
    
    for j  in range(len(oranges)):
        s2 = 0 
        s2 = b + oranges[j]
        if(s2 >= s and s2 <= t):
            count2 += 1
    print(count1)
    print(count2)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
