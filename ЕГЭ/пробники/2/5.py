# for n in range(1,100):
#     a=bin(n)[2:]
#     b=str(a.count('1')%2)
#     a=a+b
#     a=a+b
#     v=int(a,2)
#     if v<64:
#         print(v)
for n in range(1,100):
    b= n%4
    r=n-b
    m=bin(r)[2:]
    j = str(m.count('1') % 2)
    m=m+j
    p = str(m.count('1') % 2)
    m=m+p
    h=int(m,2)
    if h<64:
        print(n)
