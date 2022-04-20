import os
import sys

def getMoneySpent(keyboards, drives, b):
    
    ma = -1
    for k in keyboards:
        for d in drives:
            if k+d <= b:
                ma=max(ma, k+d)
            
    return ma