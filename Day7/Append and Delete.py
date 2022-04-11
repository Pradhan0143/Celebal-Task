import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    # Write your code here
    c = 0
    
    for i,j in zip(s, t):
        if i == j:
            c+=1
        
    tl = len(s) + len(t)
    
    if tl <= 2*c + k and tl%2 or tl<k:
        return "Yes"
    else:
        return "No"
