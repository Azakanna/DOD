a='1'+'2'*22
while '000' in a or '222' in a:
    if '000' in a:
        a=a.replace('000','2',1)
    else:
        a=a.replace('222','0',1)
print(a)