def bonAppetit(bill, k, b):
    # Write your code here
    s=sum(bill)
    c=(s-bill[k])//2
    if b==c:
        print("Bon Appetit")
    else:
        print(b-c)