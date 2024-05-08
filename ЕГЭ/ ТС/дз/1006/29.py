otv=0
for i in range(10):
    for l in range(10):
        s='1'+str(i)+'38'+str(l)+'70'
        if int(s)%11==0:
            otv+=1
        for o in range(10):
            s1 = '1' + str(i) + '38' + str(l) + '70' +str(o)
            if int(s1)%11==0:
                otv+=1
        for o in range(10):
            for p in range(10):
                s2 = '1' + str(i) + '38' + str(l) + '70'+str(o)
                if int(s2)%11==0:
                    otv+=1
print(otv)