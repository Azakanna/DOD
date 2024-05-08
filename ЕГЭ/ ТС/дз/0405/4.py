a=6*3**1520+9**321+3**407-2022
counter=0
while a!=0:
    counter+=a%27==0
    a=a//27
print(counter)