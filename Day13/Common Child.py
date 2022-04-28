def commonChild(s1, s2):
    # Write your code here
    r = len(s1) 
    c = len(s2) 
  
    b = [[None]*(c+1) for i in range(r+1)] 
    print(b)
  
    for i in range(r+1): 
        #print (i)
        for j in range(c+1): 
            #print(j)
            if i == 0 or j == 0 : 
                b[i][j] = 0
            elif s1[i-1] == s2[j-1]: 
                #print(s1, s2)
                b[i][j] = b[i-1][j-1]+1
                #print(b[i][j])
            else: 
                b[i][j] = max(b[i-1][j] , b[i][j-1]) 
                print(b[i][j])
  
    return b[r][c]