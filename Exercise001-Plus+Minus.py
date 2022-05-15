#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positivo = 0
    negativo = 0
    cero = 0
    for i in range(n):
        if arr[i]>0:
            positivo += 1
        elif arr[i]<0:
            negativo += 1
        else:
            cero += 1
    print("%.6f" % (positivo/n))
    print("%.6f" % (negativo/n))
    print("%.6f" % (cero/n))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)