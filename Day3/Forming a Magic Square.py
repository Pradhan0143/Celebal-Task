import math
import os
import random
import re
import sys


def formingMagicSquare(s):
    
    s = sum(s, [])
    m = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[2,7,2,1,5,9,8,3,4],[8,3,4,1,5,9,6,7,2],
        [4,9,2,3,5,7,8,1,6],[4,3,8,9,5,1,2,7,6],[2,7,6,9,5,1,4,3,8],[2,9,4,7,5,3,6,1,8]]
    mc = sys.maxsize
    for M in m:
        d = 0
        for i, j in zip(s, M):
            d = d + abs(i-j)
        mc = min(mc, d)
    return mc