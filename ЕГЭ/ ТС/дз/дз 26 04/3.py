counter=0
for a in range(10):
    for b in range(10):
        s='1'+str(a)+'38'+str(b)+'70'
        if int(s)%11==0:
            counter+=1
        for c in range(10):
            s='1'+str(a)+'38'+str(b)+'70'+str(c)
            if int(s)%11==0:
                counter+=1
        for d in range(10):
            for e in range(10):
                s='1'+str(a)+'38'+str(b)+'70'+str(d)+str(e)
                if int(s)%11==0:
                    counter+=1
print(counter)
