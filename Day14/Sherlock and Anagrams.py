def sherlockAndAnagrams(s):
    # Write your code here
    c=0
    d=Counter(s)
    for i in range(2,len(s)):
        sb=s[0:i]
        l=len(sb)
        d["".join(sorted(sb))]+=1
        #print(d)
        for j in range(1, len(s)):
            if j+l<=len(s):
                d["".join(sorted(s[j:j+l]))]+=1
    print(d)
    for k,v in d.items():
        c=c+v*(v-1)//2
    return c