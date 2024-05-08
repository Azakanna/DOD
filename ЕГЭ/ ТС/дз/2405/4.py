f=open(r"C:\Users\hhov0\Downloads\Задание_1_ДЗ__tcfr.txt")
s=f.readlines()
kolvo=0
for i in range(len(s)):
    s[i] = s[i][:-1]
    if i%2==1:
        if len(s[i])%2==0:
            if s[i].count('A')%3==0:
                a=s[i][:len(s)//2]
                b=s[i][len(s)//2:]
                if b.count('M') <= b.count('O'):
                    kolvo+=1
print(kolvo)
