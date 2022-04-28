def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    g = 0
    while p <= s:
        s=s-p
        p=max(p-d,m)
        #print(p)
        g=g+1
        print(g)
    return g