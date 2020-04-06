#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    s = 0
    bill.remove(bill[k])
    for i in range(len(bill)):
        s += bill[i]
    s //= 2    
    if(s == b):
        print("Bon Appetit")
    else:
        print(b - s)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
