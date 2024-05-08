# for n in range(1000):
#     r=bin(n)[2:]
#     if n%2==0:
#         t=str(r)+'0'
#     else:
#         t=str(r)+'1'
#     if t.count('1')%3==0:
#         y='11'+t[:2]
#     if t.count('11')%3!=0:
#         y='10'+t[:2]
#     j=int(y,2)
#     if j>=26:
#         print(n)
for n in range(1000):
    r=bin(n)[2:]
    if n%2==0:
        r=r+'0'
    if n%2==1:
        r=r+'1'
    if r.count('1')%3==0:
        r='11'+r[2:]
    else:
        r='10'+r[2:]
    t=int(r,2)
    if t==26 or t>26:
        print(n)
        break












































