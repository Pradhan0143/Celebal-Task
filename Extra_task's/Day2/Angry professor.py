def angryProfessor(k, a):
    # Write your code here
    c=0
    for i in a:
        if i<=0: 
            c=c+1
    if c<k:
        return "YES"
    else:
        return "NO"

