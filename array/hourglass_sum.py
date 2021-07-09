#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code her
    max_sum = -63    #max is -63 since seven 9's are possible in this hrglass shape so 7*9 = 63
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            curr_sum = sum(arr[i][j:j+3] + arr[i+2][j:j+3]) + arr[i+1][j+1]
            if (curr_sum >= max_sum):
                max_sum = curr_sum   #update max_sum
    return max_sum

   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
