f= open (r"C:\Users\hhov0\Downloads\17__sfq3.txt")
a=f.readlines()
b=[]
for i in a:
    b.append(int(i))
kolvo=0
maximus= -10000000000000
for i in range (0,len(b)-1):
    # n=b[i]
    # m=b[i+1]
    if (b[i]+b[i+1])%2==0:
        kolvo= kolvo+1
        if b[i]>maximus:
            maximus=b[i]
        if b[i+1]>maximus:
            maximus=b[i+1]
print(kolvo,maximus)








