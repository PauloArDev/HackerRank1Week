#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # Solution from youtube
    #    x=sorted(arr)
    #   print(sum(x[:-1]), sum(x[1:]))
    x=sorted(arr)
    y=sorted(arr)
    x.pop(0)
    y.pop(4)
    print(sum(y), sum(x))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)