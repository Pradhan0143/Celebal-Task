import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**8)

count = 0
def countLuck(matrix, k):
    # Write your code here
    r = len(matrix)
    c = len(matrix[0])
    global count
    count = 0
    
    for i in range(r):
        matrix[i] = list(matrix[i])
        
    xi = [0, 0, 1, -1]
    yi = [1, -1, 0, 0]
    def neighbor(i, j):
        temp = 0
        for x,y in zip(xi, yi):
            if 0 <= i+x < r and 0 <= j+y < c and matrix[i+x][j+y] != 'X':
                temp += 1
        return temp 
          
    def dfs(i,j,matrix):
        global count
        if matrix[i][j] == '*':
            return True
        
        matrix[i][j] = 'v'
        flag = False
        for x, y in zip(xi, yi):
            if 0 <= i+x < r and 0 <= j+y < c and matrix[i+x][j+y] in ['.', '*']:
                flag = dfs(i+x, j+y, matrix)
                if flag == True:
                    matrix[i][j] = '0'
                    
                    count += 1 if neighbor(i, j) > 2 else 0
                    return flag
        matrix[i][j] = '.'
        return flag
           
        
        
    flag = False
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 'M':
                matrix[i][j] = '.'
                flag = dfs(i,j,matrix)
                count -= 1 if neighbor(i, j) > 2 else 0
                count += 1 if neighbor(i, j) > 1 else 0
                break
            
    if flag and count == k:
        return "Impressed"
    else:
        return "Oops!"
