f=open(r"C:\Users\hhov0\Downloads\Задание_2_ДЗ__tcfu.txt")
s=f.readline()
s=s.replace('RA','?')
s=s.replace('RE','?')
kolvo=1
maxim=0
for i in range (len(s)-1):
    if s[i]=='?' and s[i+1]=='?':
        kolvo+=1
        maxim=max(kolvo,maxim)
    else:
        kolvo=1
print(maxim)