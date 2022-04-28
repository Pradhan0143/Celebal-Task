def cavityMap(grid):
    # Write your code here
    r = []
    n = len(grid)
    
    for i in range (1, n-1):
        for j in range (1, n-1):
            v=grid[i][j]
            mx=max((grid[i-1][j]), (grid[i+1][j]), (grid[i][j-1]), (grid[i][j+1]))
            #print(mx)
            
            if v > mx:
                print(v,mx)
                r.append([i,j])
    
    for k in r:
        r=k[0]
        c=k[1]
        grid[r]=grid[r][:c]+'X'+grid[r][c+1:]
    
    return grid