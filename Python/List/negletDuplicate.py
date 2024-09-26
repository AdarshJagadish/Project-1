l=[2,5,6,4,9,1,5,3,5,4,7,5,6,3,2,1]
print(l)
for i in l:
    if l.count(i)>=2:
        l.pop(i)    
print(l)