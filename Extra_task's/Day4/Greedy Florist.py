def getMinimumCost(k, c):
    res = 0
    c = 0

    flowers = sorted(c, key=lambda x: -x)
    #flowers = c[:-1]
    
    for el in flowers:
        res += el * (1 + c//k)
        c += 1
        
    return res