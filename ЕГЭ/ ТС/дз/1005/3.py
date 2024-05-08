f=open(r"C:\Users\hhov0\Downloads\3.txt")
s=f.readline()
maks=0
counter=1
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        counter+=1
        if counter>maks:
            maks=counter
    else:
        counter=1
print(maks)