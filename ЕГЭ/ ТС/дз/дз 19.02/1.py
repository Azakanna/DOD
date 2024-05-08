f=open (r"C:\Users\hhov0\Downloads\Задание_17__rg3t.txt")
a=f.readlines()
b=[]
for i in a:
    b.append(int(i))
summchis=0
srarfm = 0
kolvo = 0
for i in range (0,len(b)-1):
    n=b[i]
    m=b[i+1]
    if n>750 and m>750:
        kolvo= kolvo+1
for i in range(0,len(b)):
    g=b[i]
    if g>-1000000:
        summchis=summchis+g
srarfm=summchis%len(b)
print(srarfm,kolvo)
