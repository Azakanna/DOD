a='1'*100+'2'*100+'3'
while '12' in a or '23' in a or '33333' in a:
    if '12' in a:
        a=a.replace('12','2',1)
    elif '23' in a:
        a=a.replace('23','33',1)
    elif '333' in a:
        a=a.replace('3333','3',1)
print(a)