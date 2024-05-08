f = open(r'C:\Users\hhov0\Downloads\6.txt')
b = int(f.readline())
m = [[] for i in range (10001)]
ryad=0
maximus=0
for j in range (b):
    x,y=map(int,f.readline().split())
    if not(y in m[x]):
        m[x]+=[y]
for i in range(1,10001):
    m[i].sort()
for j in range(1,10001):
    symma=1
    for i in range(len(m[j])-1):
        if m[j][i+1]-m[j][i]==1:
            symma+=1
            if symma>maximus:
                maximus=symma
                ryad=j
        else:
            symma=1
print(maximus,ryad)




















