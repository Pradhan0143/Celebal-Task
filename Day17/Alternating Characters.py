def alternatingCharacters(s):
    # Write your code here
    c=0
    l=len(s)
    
    for i in range(1, l):
        if s[i] == s[i-1]:
            c=c+1
           
    return c