
import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    
    r = s  + m-1
    r = r%n
    if r == 0:
        return n
    return r