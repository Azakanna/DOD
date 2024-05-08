def prot(x,y,z):
    a=[]
    xy=(x==-y)
    yz=(y==-z)
    xz=(x==-z)
    if xy==True:
        return (x*y)*-1
    if yz==True:
        return (y*z)*-1
    if xz==True:
        return (x*z)*-1
    return 0
def proi(x):
    summa=1
    while x>0:
        summa*=x%10
        x=x//10
    if summa%100==42:
        return True
    return False

f=open(r"C:\Users\hhov0\Downloads\17_2 (3).txt")
n=[int(x) for x in f]
maks=0
minim=10**8
kolvo=0
for i in range(len(n)):
    if proi(n[i])==True:
        if n[i]>maks:
            maks=n[i]
for i in range(len(n)-2):
    if prot(n[i],n[i+1],n[i+2])>0 and maks>n[i] and maks>n[i+1] and maks>n[i+2] :
        minim=min(minim,prot(n[i],n[i+1],n[i+2]))
        kolvo+=1
print(kolvo,minim)



