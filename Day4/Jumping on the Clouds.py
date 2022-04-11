import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    
    j = 0
    i = 0
    while i < n-1:
        if i+2 < n and c[i+2]==0:
            j+=1
            i+=2
        elif i+1 < n and c[i+1]==0:
            j+=1
            i+=1
    return j
