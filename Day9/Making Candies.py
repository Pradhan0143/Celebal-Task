import math
import os
import random
import re
import sys


def minimumPasses(m, w, p, n):
    # Write your code here
    d = 0
    c = 0
    r = math.ceil(n / (m * w))

    while d < r:
        if p > c:
            dN = math.ceil((p - c) / (m * w))
            c += dN * m * w
            d += dN

        diff = abs(m - w)
        av = c // p
        pc = min(diff, av)

        if m < w:
            m += pc
        else:
            w += pc

        rest = av - pc
        m += rest // 2
        w += rest - rest // 2
        c -= av * p

        c += m * w
        d += 1

        remainingCandies = max(n - c, 0)
        r = min(r, d + math.ceil(remainingCandies / (m * w)))
    
    return r


'''
import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    # Write your code here
    d = 0
    c = 0
    r = math.ceil(n / (m * w))
    print(r)

    while d < r:
        if p > c:
            dN = math.ceil((p - c) / (m * w))
            c += dN * m * w
            d += dN
            print(d)

        diff = abs(m - w)
        av = c // p
        pc = min(diff, av)
        print(pc)

        if m < w:
            m += pc
            print(m)
        else:
            w += pc
            print(w)

        rest = av - pc
        print(rest)
        m += rest // 2
        print(m)
        w += rest - rest // 2
        print(w)
        c -= av * p
        print(c)

        c += m * w
        d += 1

        remainingCandies = max(n - c, 0)
        r = min(r, d + math.ceil(remainingCandies / (m * w)))
    
    return r


'''