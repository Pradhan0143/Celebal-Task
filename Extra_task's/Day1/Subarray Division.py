def birthday(s, d, m):
    # Write your code here
    c=0
    t=sum(s[:m])
    ls=len(s)
    
    if t==d:
        c=c+1
    
    for i in range (m, ls):
        t=t+s[i]
        t=t-s[i-m]
        if t==d:
            c+=1
    return c