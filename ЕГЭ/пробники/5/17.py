f=open(r'C:\Users\hhov0\Downloads\Задание_17__Школково___1fyy8__1k8ky.txt')
a=[int(x) for x in f]
kolvo=0
kolvo3=0
maxim=-10000000
for i in range(len(a)):
    if a[i]%3==0:
        kolvo3+=1
for l in range(len(a)-1):
    print(l)
    if (a[l]<0 or a[l+1]<0) and (a[l]+a[l+1]<kolvo3):
        kolvo+=1
        if a[l]+a[l+1]>maxim:
            maxim=a[l]+a[+1]
print(kolvo,maxim)


