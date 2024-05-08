f=open(r"C:\Users\hhov0\Downloads\24.txt")
s=f.readline()
maks=0
kolvo=1
s=s.replace('RE','*')
s=s.replace('RA','*')
for i in range(len(s)-1):
    if s[i]=='*' and s[i+1]=='*':
        kolvo+=1
        maks=max(kolvo,maks)
    else:
        kolvo=1
print(maks)