counter=0
zapret=['14','41','34','43','54','45','47','74']
for a in '1234567':
    for b in '01234567':
        for c in '01234567':
            for d in '01234567':
                for e in '01234567':
                    slovo=a+b+c+d+e
                    if slovo.count('4')==2:
                        if all(x not in slovo for x in zapret):
                            counter+=1
print(counter)


