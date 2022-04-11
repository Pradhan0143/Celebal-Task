import math
import os
import random
import re
import sys
from collections import Counter

def pairs(k, arr):
    
    d = Counter(arr)
    p = 0
    
    for i in arr:
        if i+k in d:
            p=p+1
        if i-k in d:
            p=p+1
        del d[i]
    return p
