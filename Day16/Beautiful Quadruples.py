def beautifulQuadruples(a, b, c, d):
    #
    # Write your code here.
    #
    #print(a,b,c,d)
    a,b,c,d=sorted([a,b,c,d])
    #print(a,b,c,d)
    l=[0]*3000
    count=0
    t=0
    
    for i in range(1, c+1):
        for j in range(i, d+1):
            l[i^j]+=1
            t+=1
        
    for i in range(1, b+1):
        for j in range(1, min(a, i) + 1):
            count+=t-l[i^j]
                
        for k in range(i, d+1):
            l[i^k]-=1
            t-=1
            
    return count
