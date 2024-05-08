counter=0

maximus=0
for i in range(591645,592846):
    kolvo = 0
    for l in range(1,int(i**0.5)+1):
        if i%l==0:
            kolvo+=1
    if kolvo>maximus:
        maximus=kolvo
        counter=i
print(counter)