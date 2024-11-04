l=[10,1,3,5,8]
smallest=l[0]
largest=l[0]
for i in l:
    if i<smallest:
        smallest=i
    elif i>largest:
        largest=i
print('The smallest amoung the list is ',smallest)
print('The largest amoung the list is ',largest)