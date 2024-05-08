s=91 * '1'
while ('2222' in s) or ('1111' in s):
    if ('2222' in s):
        s=s.replace('2222','11',1)
    if ('1111' in s ):
        s=s.replace('1111','22',1)
print(s)
