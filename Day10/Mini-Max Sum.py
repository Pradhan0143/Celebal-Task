import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    s = 0
    n = len(arr)
    mn = 10**9
    mx = 0
    for i in range(n):
        s += arr[i]
        mn = min(mn, arr[i])
        mx = max(mx, arr[i])
        
    print(s-mx, s-mn)
