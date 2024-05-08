a='1'*99
while '111' in a:
    a=a.replace('111','22',1)
    a=a.replace('222','11',1)
print(a)