a=(2**345+8**65-4**130)*(8**123-2**89+4**45)
counter=0
while a>0:
    b=a%8
    counter+=b
    a=a//8
print(counter)