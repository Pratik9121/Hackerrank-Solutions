import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    s = 1 
    if n == 0:
        return 1
    for i in range(1,n+1):
        if i % 2 == 1:
            s *= 2
        else:
            s += 1
    return s


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
