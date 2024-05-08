counter=0
for x in range(10,100):
    q=x%2
    w=x%3
    e=x%5
    y=str(q)+str(w)+str(e)
    y1=int(y)
    if y1==100:
        counter+=1
print(counter)