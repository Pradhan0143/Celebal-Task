import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    
    '''p = 0
    c = set()
    a = len(ar)
    for i in range (a):
        if ar[i] not in c:
            c.add(ar[i])
        else:
            p += 1 
            c.remove(ar[i])
    return p'''
    c = Counter(ar)
    p = 0
    for i in (c):
        p += c[i] // 2
    return p
