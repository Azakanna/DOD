a='11'*170 + '3'*100+'2'*7
while '11' in a:
    a=a.replace('112' , '4', 1)
    a = a.replace('113', '2', 1)
    a = a.replace('42', '3', 1)
    a = a.replace('43', '1', 1)
print(a)
