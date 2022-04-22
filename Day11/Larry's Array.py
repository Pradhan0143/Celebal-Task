def larrysArray(A):
    # Write your code here
    print (A)
    s = 0
    a = A
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                s=s+1
            
    if s%2 == 0:
        return "YES"
    else:
        return "NO"