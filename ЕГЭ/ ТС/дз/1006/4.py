a='1'+'0'*100+'333'
while '10' in a or '11' in a or '330' in a:
    if '10' in a:
        a=a.replace('10','1',1)
    elif '11' in a:
        a=a.replace('11','3',1)
    elif '330' in a:
        a=a.replace('330','100',1)
summa=1
for i in range(len(a)):

    summa*=int(a[i])
print(summa)