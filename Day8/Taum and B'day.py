import math
import os
import random
import re
import sys


def taumBday(b, w, bc, wc, z):
    # Write your code here
    r = 0
    gb = b * bc
    gw = w * wc
    cb = bc*(w+b)
    cw = wc*(w+b)
    r = min(gb + gw, cb + w*z, cw + b*z)
    return r
