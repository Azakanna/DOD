a='2'*2+'1'*2023+'2'*2
while '211' in a or '112' in a:
    a=a.replace('11','1',1)
    if '21' in a:
        a=a.replace('21','12',1)
    else:
        a=a.replace('12','1',1)
print(a)