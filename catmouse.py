import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    caty1=0
    caty2=0
    caty1=x-z
    caty2=y-z
    r=abs(caty1)
    m=abs(caty2)
    if r>m:
        return 'Cat B'
    elif r==m:
        return 'Mouse C'
    else:
        return 'Cat A'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()






