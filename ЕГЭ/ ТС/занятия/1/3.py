n=str(214)
m=str(165)
j=0
g=0
k=8
for i in range (len(n)):
    c= int(n[i])
    h= len(n)-1-i
    o= int(m[i])
    q= len(m)-1-i
    g+=c * k ** h
    j+=o * (k+1) ** q
print(g,j)
# ответ 8