def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    totalapples=0
    totaloranges=0
    lenapple=len(apples)
    lenoranges=len(oranges)
    
    for i in range (lenapple):
        if s<= a+apples[i] <=t:
            totalapples=totalapples+1
            
    for i in range (lenoranges):
        if s<= b+oranges[i] <=t:
            totaloranges=totaloranges+1
    
    print(totalapples)
    print(totaloranges)
    