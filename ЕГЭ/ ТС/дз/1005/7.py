f=open(r"C:\Users\hhov0\Downloads\7.txt")
s=f.readline()
counter=1
maks=0
g='AEIOUY'
for i in range(len(s)-1):
    if (s[i] in g) and (s[i+1] not in g) or (s[i] not in g) and (s[i+1] in g):
        counter+=1
        maks=max(maks,counter)
    else:
        counter=1
print(maks)
