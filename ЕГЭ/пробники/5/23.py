def f(st,fin,flag10):
    if st==10:
        flag10=True
    if st==fin and flag10==True:
        return 1
    if (st==fin and flag10==False) or st<fin:
        return 0
    x=f(st-2,fin,flag10)
    y=f(st//2,fin,flag10)
    return x+y
print(f(40,2,False))