for i in range(100,120):
    a='1'*i
    while '333' in a or '111' in a:
        a=a.replace('333','11',1)
        a=a.replace('111','3',1)
    if a=='3311':
        print(i)