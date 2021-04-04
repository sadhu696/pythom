a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    if b>=c:
        print(a)
        print(c)
        print(b)
    else:
        print(a)
        print(b)
        print(c)
elif a>=b and a <=c:
    print(c)
    print(b)
    print(a)
elif a<=b and a>=c:
    print(b)
    print(c)
    print(a)
elif a<=b and a<=c:
    if b>=c:
        print(b)
        print(a)
        print(c)
    else:
        print(c)
        print(a)
        print(b)