l=[100,200,300,100,200,400,500,100,200]
l2=[]
for i in l:
    if i in l2:
        pass
    else:
        l2.append(i)
print(l2)