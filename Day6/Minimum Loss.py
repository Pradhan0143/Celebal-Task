import math
import os
import random
import re
import sys

def minimumLoss(price):
    
    d = {}
    for i,p in enumerate(price):
        d[p]=i
    price.sort()
    
    mv = sys.maxsize
    for i in range(1, len(price)):
        if d[price[i-1]] > d[price[i]]:
            mv = min(mv, price[i] - price[i-1])
    return mv
