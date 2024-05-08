s=open(r"C:\Users\hhov0\Downloads\24_3 (1).txt").readline()
s=s.replace('OSR','1')
s=s.replace('RSO','1')
k=1
m=0
for i in range (len(s)-1):
    if s[i]=='1' and s[i+1]=='1':
        k+=1
        m=max(m,k)
    else:
        k=1
print (m*3)