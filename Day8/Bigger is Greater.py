import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    
    n = len(w)
    w = list(w)
    r = ''
    i = n-2
    while i >= 0 and w[i] >= w[i+1]:
        i -= 1
    
    if i == -1:
        r = "no answer"
    else:
        j = n-1
        while j >= i and w[j] <= w[i]:
            j = j - 1
            
        w[i], w[j] = w[j], w[i]
        w = "".join(w)
        r = w[:i+1] + w[i+1:][::-1] # print in string in reverce order 
    return r
