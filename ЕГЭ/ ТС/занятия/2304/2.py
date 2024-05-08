counter=0
for a in range(1,10):
    for b in range(10):
        s=str(a)+'3579'+str(b)+'6'
        if int(s)%7==0:
            counter+=1
        for c in range(10):
            s = str(a) + '3579' + str(b) + '6'+str(c)
            if int(s) % 7 == 0:
                counter += 1
        for c in range(10):
            for d in range(10):
                s = str(a) + '3579' + str(b) + '6'+str(c)+str(d)
                if int(s) % 7 == 0:
                    counter += 1
print(counter)