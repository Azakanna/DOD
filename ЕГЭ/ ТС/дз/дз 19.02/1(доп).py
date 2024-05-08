for i in range(4):
    x=str(i)
    n=int(('20'+x+'3'),4)
    m=int(('1'+x+'32'),4)
    if (n+m)%3==0:
        print((n+m)//3)

