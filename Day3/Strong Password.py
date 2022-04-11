import math
import os
import random
import re
import sys


def minimumNumber(n, password):
    
    special_characters = '!@#$%^&*()-+'
    l = [0,0,0,0]
    
    for char in password:
        if char.isdigit():
            l[0] = 1
        elif char.islower():
            l[1] = 1
        elif char.isupper():
            l[2] = 1
        elif char in special_characters:
            l[3] = 1
            
    return max(6 - len(password), 4 - sum(l))