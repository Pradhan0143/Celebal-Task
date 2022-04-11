import math
import os
import random
import re
import sys


def highestValuePalindrome(s, n, k):
    
    s = list(s)
    v = [0] * n
    l = 0
    r = n-1
    
    while l <= r:
        if s[l] != s[r]:
            if s[l] > s[r]:
                s[r] = s[l]
                v[r] = 1
            else:
                s[r] = s[l]
                v[l] = 1
            k -= 1
        l += 1
        r -= 1
        
    if k < 0:
        return "-1"
    
        l = 0
        r = n-1
        while l <= r:
            if l == r and k>=1:
                s[l] = '9'
                break
            
            if s[l] < '9':
                if v[l] == 0 and v[r] == 0 and k >= 2:
                    s[l] = s[r] = '9'
                    k -= 2
                if (v[l] == 1 or v[r] == 1) and k >= 1:
                    s[l] = s[r] = '9'
                    k -= 1
            l += 1
            r -= 1
    return "".join(s)
