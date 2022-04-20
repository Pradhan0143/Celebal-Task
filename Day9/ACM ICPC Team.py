import math
import os
import random
import re
import sys


def acmTeam(topic):
    ms = 0
    c = 0
    for i in range(n):
        for j in range(i, n):
            s = 0
            for x,y in zip (topic[i], topic[j]):
                if x=='1' or y=='1':
                    s += 1
            if s>ms:
                ms=s
                c+=1
                print(c)
            elif s==ms:
                c+=1
    return[ms,c]
