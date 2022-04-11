import math
import os
import random
import re
import sys


def circularArrayRotation(a, k, queries):
    
    k = k % n
    r = []
    
    for q in queries:
        r.append(a[(n - k + q) % n])
    return r
