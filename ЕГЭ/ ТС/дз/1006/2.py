for k in range(100):
    a=str(k)
    o= k*int(a[0])
    o+=int(a[-1])
    if o==102:
        print(k)