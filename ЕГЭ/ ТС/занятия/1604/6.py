def inn(x,P):
    return P[0]<=x<=P[1]
def f(x,A):
    P=[19,56]
    Q=[32,84]
    return (((not inn(x,A)) and inn(x,Q)) <= inn(x,P))
def check(A):
    k=5
    for x in range(0,100*k):
        if f(x/k,A)==False:
            return False
    return True
minim=100000000000
k=5
for a in range(0,100*k):
    for b in range(a,100*k):
        A=[a/k,b/k]
        if check(A)==True:
            if (A[1]-A[0])<minim:
                minim=A[1]-A[0]
print(minim)
