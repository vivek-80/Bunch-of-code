#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count=0
    x=[int(d) for d in str(n)]
    for i in range(len(x)):
        if x[i]>0:
            cal=n%x[i]
            if cal==0:
                count+=1
                continue
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
