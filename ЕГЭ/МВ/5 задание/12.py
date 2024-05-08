for k in range (1,100):
    m=str(k)
    v=k*int(m[0])
    v+=int(m[-1])
    if v==280:
        print(k)
