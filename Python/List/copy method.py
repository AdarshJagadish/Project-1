# li=[1,5,3,4,8,63,7,3,7]
# li1=li
# print(li)
# print(li1)
# print(id(li))
# print(id(li1))
# li.append(20)
# print(li)
# print(li1)




li=[1,5,3,4,8,63,7,3,7]
li1=li.copy()
print(id(li))
print(id(li1))
li.pop()
print(li)
print(li1)