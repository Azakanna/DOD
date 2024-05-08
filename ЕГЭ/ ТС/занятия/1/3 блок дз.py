s=input()
otvet=0
for n in range(len(s)) :
    x=int(s[n])         #цифра
    stepen=len(s)-1-n        #stepen
    otvet+=x*9**stepen
print(otvet)