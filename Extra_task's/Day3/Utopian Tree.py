def utopianTree(n):
    # Write your code here
    spring = 0
    for i in range(n+1):
        if i%2 == 0:
            spring+=1
        else: 
            spring*2
            #print(spring)
            spring+=1
    return spring

    '''spring = 1
    
    for i in range(1, n+1):
        if i%2 != 0:
            spring*=2
        else:
            spring+=1
    return spring'''

n=int(input("enter a starting tree no. "))
st=utopianTree(n)
print(st)