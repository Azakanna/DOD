a=[0]*1000
a[22]=1
for i in range(22,2,-1):
    a[i-1]+=a[i]
    a[i-3]+=a[i]
    if i>4:
        a[i%4]+=a[i]
print(a[2])

# a=[0]*1000
# a[22]=1
# for i in reversed(range(2,23)):
#     a[i]= a[i+1] + a[i+3]
#     if i > 4:
#
#     