n=int(input())
maxim=-10000000
prmaxim=-100000
for i in range(n):
    x=int(input())
    if x>maxim:
        prmaxim=maxim
        maxim = x
    elif x>prmaxim:
        prmaxim=x
print(maxim,prmaxim)




