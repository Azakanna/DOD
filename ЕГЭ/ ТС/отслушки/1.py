print('a b c d f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f =((a and b) or (b and c))==((a <= d)and (d <= c))
                if f==1:
                    print(a,b,c,d,f)