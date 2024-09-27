l=[2,5,6,4,9,1,5,3,5,4,7,5,6,3,2,1]
l.sort()
print(l)
# for i in l:
#     if l.count(i)>=2:
#         l.remove(i)    
# print(l)


l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)