n=('1'*170)+('3'*100)+('2'*7)
while '11' in n:
    n=n.replace('112','4',1)
    n=n.replace('113','2',1)
    n=n.replace('42','3',1)
    n=n.replace('43','1',1)
print(n)