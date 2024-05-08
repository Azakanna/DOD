# f=open(r"C:\Users\hhov0\Downloads\kpolyakov.spb.ru_cms_files_ege-sym_24-253.txt")
# s=f.readline()
# maks=0
# kolvo=0
# gl='AO'
# sgl='CDF'
# for i in range(0,len(s)-2,3):
#     if (s[i] in sgl) and (s[i+2] in gl):
#         kolvo+=1
#         maks=max(kolvo,maks)
#     else:
#         kolvo=0
# kolvo=0
# for i in range(1,len(s)-2,3):
#     if (s[i] in sgl) and (s[i+2] in gl):
#         kolvo+=1
#         maks=max(kolvo,maks)
#     else:
#         kolvo=0
# kolvo=0
# for i in range(2,len(s)-2,3):
#     if (s[i] in sgl) and (s[i+2] in gl):
#         kolvo+=1
#         maks=max(kolvo,maks)
#     else:
#         kolvo=0
#
# print(maks)




f=open(r"C:\Users\hhov0\Downloads\22.txt")
s=f.readlines()
maks=0
counter=0
buk=''
pupok=''

for i in range(len(s)):
    maksim=0
    kolvo=1
    kub=''
    for l in range(len(s[i])-1):
        if s[i][l]==s[i][l+1]:
            kolvo+=1
            if kolvo>maks:
                maks=kolvo
                buk=s[i][l]
                pupok=s[i]
            if kolvo>maksim:
                maksim=kolvo
                kub=s[i][l]

        else:
            kolvo=1
    if s[i]!=pupok and maks==maksim:
        if pupok.count(buk)>s[i].count(kub):
            pupok = s[i]
            buk=kub
print(pupok.count(buk),buk)































