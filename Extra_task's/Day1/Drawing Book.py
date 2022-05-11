def pageCount(n, p):
    # Write your code here
    df=p//2
    dp=(n-p)//2
    if n%2==1:
        db=(n-p)//2
    else:
        db=(n-p)//2
    return min(df,db)