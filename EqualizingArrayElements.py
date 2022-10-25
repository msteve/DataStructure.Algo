# Given an array of integers, transform it so that at least a certain number of elements in the array are equal. To achieve this, you can perform an operation where you select an element in the array and divide it by the given division parameter using integer division. What is the minimum number of operations that must be performed to achieve this goal on a certain array?
# For example, let's say arr = [1, 2, 3, 4, 5). The desired number of equal elements is denoted as threshold = 3, and the division parameter is d = 2. If you divide the value 4 once and the value 5 once using integer division, you get the array [1, 2, 3, 2, 2], which contains 3 equal elements. There is no way to achieve this in less than 2 operations. Therefore, the answer is 2.

# Function Description 
# Complete the function min Operations in the editor below.

# minOperations has the following parameter(s):
# 	int arr[n]: an array of integers 
# 	int threshold: the minimum number of desired equal elements in the array
# 	int d: the division parameter used to divide an element in a single operation 
#         Returns:
# 	int: the minimum number of operations required to have at least threshold number of equal elements in the array

import math
import os
import random
import re
import sys

from collections import defaultdict


#
# Complete the 'minOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER threshold
#  3. INTEGER d
#

def minOperations(arr, threshold, d):
    # dp[i] := [count of i values, number of steps]
    dp = defaultdict(lambda: [0, 0])
    arr.sort()
    ans = sys.maxsize
    for x in arr:
        steps = 0
        while True:
            dp[x][0] += 1
            dp[x][1] += steps
            if dp[x][0] >= threshold:
                ans = min(ans, dp[x][1])
            if x == 0:
                break
            x //= d
            steps += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    threshold = int(input().strip())

    d = int(input().strip())

    result = minOperations(arr, threshold, d)

    fptr.write(str(result) + '\n')

    fptr.close()