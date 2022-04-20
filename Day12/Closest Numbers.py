import math
import os
import random
import re
import sys

def closestNumbers(arr):
    
    p = []
    md = 10**7
    arr.sort()
    a = len(arr)
    
    for i in range(1, a):
        d = abs(arr[i-1] - arr[i])
        
        if d < md:
            md = d
            p = ([arr[i-1], arr[i]])
        elif d == md:
            p.extend([arr[i-1], arr[i]])
    return p
