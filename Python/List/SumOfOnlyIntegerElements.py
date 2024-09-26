l=[10,11,8,5,2,12,10,'abc','a','l','f']
a=0
print(l)
for i in l:
    if type(i)==int or type(i)==float:
        a=a+i
print("The sum of elements in the list is ",a)