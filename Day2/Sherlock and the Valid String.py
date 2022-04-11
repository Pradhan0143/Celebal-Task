import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
        
    c = Counter(s)
    
    if len(set(c.values())) == 1:
        return"YES"
    
    elif len(set(c.values())) > 2:
        return"NO"
    
    else:
        for key in c:
            c[key] = c[key] - 1
            temp = list(c.values())
            
            try:
                temp.remove(0)
            except:
                pass
            if len(set(temp)) == 1:
                return "YES"
            else:
                c[key] = c[key] + 1
        return"NO" 
