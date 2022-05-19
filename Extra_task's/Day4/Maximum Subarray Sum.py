'''
def maximumSum(a, m):
    # Write your code here
    arr=a
    c=0
    for i in range (len(arr)):
        arr[i]=i
        #print(arr[i])
        c+=1
        if arr[i]%m == 0:
                c+=1
                print(c)
    
        
    return c
'''

def maximumSum(a, m):
    # Write your code here
    l=[]
    sum_arr=0
    res=0
    
    for i in range (n):
        sum_arr=sum_arr+a[i]
        sum_arr=sum_arr%m
        indx=bisect_right(l,sum_arr)
        print(sum_arr)
        print(l)
        print(indx)
        if indx !=len(l):
            res=max(res,sum_arr-l[indx]+m)
            l.insert(indx,sum_arr)
        else:
            res=max(res,sum_arr)
            l.append(sum_arr)
            
    return res