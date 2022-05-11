def nonDivisibleSubset(k, s):
    # Write your code here
    re=[0]*k
    for i in s:
        re[i%k]=re[i%k]+1
    
    mx=0
    mx=mx+min(re[0],1)
    if k%2==0:
        mx=mx+min(re[k//2],1)
    
    for i in range (1,k//2+1):
        if i != k-i:
            mx=mx+max(re[i],re[k-i])
            
    return mx