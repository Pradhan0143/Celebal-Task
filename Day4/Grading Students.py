import math
import os
import random
import re
import sys


def gradingStudents(grades):
    
    r = []
    for grade in grades:
        if grade>=38:
            mod5 =  grade % 5
            
            if mod5>=3:
                grade += (5-mod5)
        r.append(grade)
    return r
