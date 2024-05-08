def pr(n):
    r=bin(n)[2:]
    if r.count('1')==3:
        return True
    else:
        return False

f=open(r"C:\Users\hhov0\Downloads\17__vrwb.txt")
s=f.readlines()
kolvo=0
maks=0
summa=0
for i in range(len(s)):
    if pr(int(s[i]))==True:
        if pr(int(s[i+1]))==True:
            if pr(int(s[i+2]))==True:
                kolvo+=1
                summa+=max(int(s[i]),int(s[i+1]),int(s[i+2]))
                maks=max(maks,summa)
print(kolvo,maks)
