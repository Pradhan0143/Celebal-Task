import math
import os
import random
import re
import sys
from math import *

def encryption(s):
    
    n = len(s)
    r = floor(sqrt(n))
    c = ceil(sqrt(n))
    r = []
    
    for i in range(c):
        temp = []
        j = 0
        while i+j<n:
            temp.append(s[i+j])
            j+=c
        r.append("".join(temp))
    return " ".join(r)
