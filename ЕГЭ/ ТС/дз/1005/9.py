f =open(r"C:\Users\hhov0\Downloads\10.txt")
s=f.readline()
counter=3
maks=0
for i in range(len(s)-4):
    # if (s[i]+s[i+1]+s[i+2]+s[i+3])!='XXYZ':
    if s[i:i+4]!='XXYZ':
        counter+=1
        if counter>maks:
            maks=counter
    else:
        counter=3
print(maks)
