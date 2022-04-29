def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x.sort()
    c = 0
    i = 0
    while i<n:
        l = x[i] + k
        #print(l)
        while i<n and x[i]<=l:
            i = i + 1
            #print(i)
        i = i - 1
        print(i)
        c = c + 1 
        print(c)
        l = x[i] + k
        while i<n and x[i]<=l:
            i = i + 1
            #print(i)
    return c