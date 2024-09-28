a=input('Enter String')
# rev=''
# for i in a:                             # Using for loop
#     rev=i+rev
# print(rev)



b=len(a)
i=0
rev=''
while i<b:
    # print(a[i])                     #Using While Loop
    rev=a[i]+rev
    i+=1
print(rev)