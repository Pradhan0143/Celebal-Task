import math
import os
import random
import re
import sys
from collections import Counter

def cutTheSticks(arr):
    
    n = len(arr)
    s = Counter(arr)
    r = []
    for i in sorted(s.keys()):
        print(s.keys())
        r.append(n)
        n -= s[i]
    return r
