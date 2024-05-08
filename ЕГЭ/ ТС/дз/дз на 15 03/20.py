
def f(a,b):
    maximum=-10
    for i in range (1,a+1):
        if (a%i==0) and (b%i==0):
            maximum = i
    return maximum
print(f(37415,256560))

