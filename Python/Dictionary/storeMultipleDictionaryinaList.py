l=[]
limit=int(input('Enter limit'))
for i in range(limit):
    name=input('name')
    age=int(input('age'))
    l.append({'name':name,'age':age})
print(l)