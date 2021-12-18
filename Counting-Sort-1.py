#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # maxium = max(arr)
    newarr = [0] * 100
    print(newarr)
    for index, element in list(enumerate(arr)):
        #         print(element)
        newarr[element] = newarr[element] + 1
    # Write your code here

    print(newarr)
    return (newarr[i] for i in range(100))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
