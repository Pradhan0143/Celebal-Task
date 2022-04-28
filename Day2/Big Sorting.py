import math
import os
import random
import re
import sys

def bigSorting(unsorted):
    unsorted = list(map(int, unsorted))
    unsorted.sort()
    unsorted = list(map(str, unsorted))
    print(unsorted)
    