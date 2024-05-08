f=open(r"C:\Users\hhov0\Downloads\Задание_3_ДЗ__tcfv.txt")
s=f.readline()
s=s.replace('SM','S*M')
s=s.replace('MS','M*S')
a=s.split('*')
maxim=0
for i in range(len(a)):
    if len(a[i])>maxim:
        maxim=len(a[i])
print(maxim)













# # alp=sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
# kolvo=0
# maxim=0
# for i in range(len(a)):
#     if a[i] in alp:
#         kolvo+=1
#         maxim=max(kolvo,maxim)
# print(maxim)