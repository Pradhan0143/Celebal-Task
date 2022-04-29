def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    t = 0 # kadm 
    obs = {} # pairs
    a=r_q
    b=c_q
    
    for i,j in obstacles:
        if i in obs:
            obs[i][j]=1 #start chas in 1
        else:
            obs[i]={j:1} # pair i of j 
    
    def limit(x,y):
        return 1 if 1<=x<=n and 1<=y<=n else 0
    
    def check(x, y, xi, yi):
        c=0
        x=x+xi
        y=y+yi
        
        while limit(x,y) and obs.get(x, {}).get(y,0)==0:
            c=c+1
            x=x+xi
            y=y+yi
        return c
    
    r=[0,0,-1,1,-1,1,-1,1]
    c=[1,-1,0,0,-1,1,1,-1]
    
    for i,j in zip(r,c):
        t=t+check(a,b,i,j)
        
    return t