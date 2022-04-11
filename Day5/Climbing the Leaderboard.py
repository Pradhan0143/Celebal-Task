import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    # Write your code here
    r = list(set(ranked))
    r.sort()
    n = len(r)
    i = 0
    res = []
    
    for p in player:
        while i<n and r[i]<=p:
            i+=1
        res.append(n - i + 1)
    return res
