d={'Rollno':1,'name':'anu','age':20,'mark':20}
d['name']='amal'
print(d['name'])
d['place']='ekm'
print(d)
if d['Rollno']==1:
    print("Yes")
else:
    print("No")
for i in d:
    # print(i)
    # print(d[i])
    print(i,d[i])