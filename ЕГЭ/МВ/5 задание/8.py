for y in range (3,10000):
    x=bin(y)[2:]
    x+=x[1]+x[0]
    x='1'+(x)
    b=int(x,2)
    if b>50:
        print(b)
        break