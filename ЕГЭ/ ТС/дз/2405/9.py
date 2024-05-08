# f=open(r"C:\Users\hhov0\Downloads\Задание_6_ДЗ__tcgb.txt")
# s=f.readline()
# kolvo=5
# maks=5
# for i in range(len(s)-4):
#     if s[i]!=s[i+3] or s[i+1]!=s[i+4] or s[i+2]!=s[i+5]:
#         kolvo+=1
#         maks=max(kolvo,maks)
#     else:
#         kolvo=5
# print(maks)
def dels(n):
    a=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            o=n//i
            a.append(i)
            a.append(o)
            if n ** 0.5 == i:
                a.remove(i)
    return sorted(a)
print(dels(18))