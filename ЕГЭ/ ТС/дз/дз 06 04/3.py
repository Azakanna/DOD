n=('5'*10)+('4'*10)+('2'*10)+('7'*10)
while '54' in n or '27' in n:
    if '55' in n:
        n=n.replace('55','7',1)
    elif '22' in n:
        n=n.replace('22','7',1)
    if '44' in n:
        n=n.replace('44','4',1)
    elif '77' in n:
        n=n.replace('77','7',1)
p=n.count('7')
print(p)
