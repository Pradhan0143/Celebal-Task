def organizingContainers(container):
    # Write your code here
    r = [0] * n
    c = [0] * n
    
    for i in range (n):
        for j in range (n):
            r[i] = r[i] + container[i][j]
            
            c[i] = c[i] + container[j][i]
        
            
    if sorted(r)==sorted(c):
        return "Possible"
    else:
        return "Impossible"