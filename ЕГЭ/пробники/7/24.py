f=open(r"C:\Users\hhov0\Downloads\24-1__yrq9.txt")
s=f.readline()
maks=-10**8
chis='02468'
alp='QWERTYUIOPASDFGHJKLZXCVBNM'
for i in range(len(alp)):
    s=s.replace(alp[i],'*')
s=s.split('*')
for l in range(len(s)):
    if len(s[l])>0:
        flag=True
        for q in range(5):
            if  chis[q]  in s[l]:
                flag=False
        if flag==True:
            b=int(s[l])
            maks=max(maks,b)
print(maks)




