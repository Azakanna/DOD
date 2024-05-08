counter=0
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                s=str(a)+'9'+str(b)+'7'+str(c)+str(d)
                if int(s[0])+int(s[1])+int(s[2])==int(s[3])+int(s[4])+int(s[5]):
                    counter+=1
print(counter)

