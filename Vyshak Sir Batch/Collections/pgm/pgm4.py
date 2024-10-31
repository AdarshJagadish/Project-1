l=[]
limit=int(input('Enter Limit '))
for i in range(limit):
    li=input("Enter the key ")
    l.append(li)
print(l)
d=dict.fromkeys(l,'null')
print(d)