n='1'+ ('0'*75)
while '10' in n or '1' in n:
    if '10' in n:
        n=n.replace('10','001',1)
    else:
        n=n.replace('1','00',1)
p=n.count('0')
print(p)