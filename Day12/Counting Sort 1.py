import math
import os
import random
import re
import sys

def countingSort(arr):
    arr.sort()
    print(arr)
    a=len(arr)
    print(a)
    c = [0]*100
    for n in arr:
        c[n] += 1
        
    return c
