a=25**20+4*5**11-2
s=''
while a>0:
    s=str(a%5)+s
    a=a//5
print(s.count('3'))