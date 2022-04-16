import math
import os
import random
import re
import sys


def beautifulTriplets(d, arr):
    # Write your code here
    c = 0
    for x in arr:
        if d+x in arr and 2*d+x in arr:
            c=c+1
    return c
    