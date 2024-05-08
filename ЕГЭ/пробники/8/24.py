f=open(r"C:\Users\hhov0\Downloads\24__vrwj.txt")
s=f.readlines()
minim=10**8
pupok=''
maks=0
p=0
a=[0]*26
alp=sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
for i in range(len(s)):
    p += s[i].count('W')
    counter=0
    for l in range(len(s[i])-1):
        if ord(s[i][l])+1==ord(s[i][l+1]):
            counter+=1
    if counter>0 and counter<minim:
        minim=counter
        pupok=s[i]
for q in range(26):
    a[q]=(pupok.count(alp[q]))

print('W',p)










