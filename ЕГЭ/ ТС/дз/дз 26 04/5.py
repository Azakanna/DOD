counter=0
for a in range(10):
    for b in range(10):
        s='829'+str(a)+'17'+str(b)
        if int(s)%31==0:
            counter+=1
        for c in range(1,10):
            s=str(c)+'829'+str(a)+'17'+str(b)
            if int(s)%31==0:
                counter+=1
        for c in range(1,10):
            for d in range(10):
                s=str(c)+str(d)+'829'+str(a)+'17'+str(b)
                if int(s)%31==0:
                    counter+=1
print(counter)