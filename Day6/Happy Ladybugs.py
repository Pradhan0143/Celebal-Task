import math
import os
import random
import re
import sys
from collections import Counter

def happyLadybugs(b):
    
    b = Counter(b)
    
    for i,j in b.items():
        if i != "_" and j == 1:
            return "NO"
    
    if b["_"] > 0:
        return "YES"
    else:
        p = 0
        for i in range(len(b)-1):
            if b[i]==b[i+1]:
                p=p+1
            elif p > 0:
                p = 0
            else:
                return "NO"
            
        return "YES"
