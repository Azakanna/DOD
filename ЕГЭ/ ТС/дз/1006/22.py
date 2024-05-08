f=open(r"C:\Users\hhov0\Downloads\24_2 (1).txt")
s=f.readline()
ABBA=0
BABA=0
BAAB=0
for i in range(len(s)-3):
    if (s[i:i+4]=='ABBA'):
        ABBA+=1
    if (s[i:i+4]=='BABA'):
        BABA+=1
    if (s[i : i + 4] == 'BAAB'):
        BAAB += 1
maks=max(ABBA,BABA,BAAB)
print(ABBA)
print(maks)