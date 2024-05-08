f=open(r"C:\Users\hhov0\Downloads\Задание_5_ДЗ__tcg2.txt")
s=f.readline()
alp='DSMREAIK'
KOLVO=1
MAKS=0
for i in range(len(s)-1):
    if s[i] in alp and s[i+1] in alp:
        KOLVO+=1
        MAKS=max(KOLVO,MAKS)
    else:
        KOLVO=1
print(MAKS)