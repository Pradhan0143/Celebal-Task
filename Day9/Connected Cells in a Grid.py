import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    #xi = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    #yi = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    #r = len(matrix)
    #c = len(matrix[0])
    def dfs(i,j):
        matrix[i][j]=2
        area=1
        for u,v in steps:
            x=i+u
            y=j+v
            if 0<=x<n and 0<=y<m and matrix[x][y]==1:
                area+=dfs(x,y)
        return area
        
    r=0
    steps=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    n,m=len(matrix),len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                r=max(r,dfs(i,j))
    return r
    
matrix=[[1,1,0,0,0],[0,1,1,0,0],[0,0,1,0,1],[1,0,0,0,1],[0,1,0,1,1]]
r=connectedCell(matrix)
