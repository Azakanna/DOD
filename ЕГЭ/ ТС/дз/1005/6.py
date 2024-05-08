f=open(r"C:\Users\hhov0\Downloads\6 (1).txt")
s=f.readline()
maks=0
counter=0
for i in range(len(s)):
    if s[i]=='R' and s[i+1]!='R' or s[i]!='R':
        counter+=1
        maks=max(maks,counter)
    if s[i]=='R' and s[i+1]=='R':
        counter+=1
        maks=max(maks,counter)
        counter=0
print(maks)