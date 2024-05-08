N=int(input())
M=int(input())
x=int(input())
y=int(input())
#узнаем кто из Н и М длина а кто ширина длина это l(lenght) ширина это s(short)
if M>N:
    l=M
    s=N
else:
    l=N
    s=M
if x<s-x:
    minim1=x
else:
    minim1=s-x
if y<l-y:
    minim2=y
else:
    minim2=l-y
if minim1<minim2:
    print(minim1)
else:
    print(minim2)