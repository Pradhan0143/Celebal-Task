a = int(input('enter a number'))
b = int(input('enter a number'))
c = int(input('enter a number'))

if a<b and c<b:
    print (b)
elif a<c and b<c:
    print (c)
elif b<a and c<a:
    print (a)