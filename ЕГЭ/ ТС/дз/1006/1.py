for i in reversed (range (10000,100000)):
    l=str(i)
    ch=0
    nech=0
    for r in range(len(l)):
        if r%2==0:
            ch+=int(l[r])**2
        else:
            nech+=int(l[r])**2
    minim=min(ch,nech)
    maks=max(ch,nech)
    if str(minim)+str(maks)=='027':
        print(i)
        break


    # nech=int(l[0])**2+int(l[2])**2+int(l[4])**2
    # ch=int(l[1])**2+int(l[3])**2
    # maks=max(nech,ch)
    # minim=min(nech,ch)
    # if str(minim)+str(maks)=='27':
    #     print(i)