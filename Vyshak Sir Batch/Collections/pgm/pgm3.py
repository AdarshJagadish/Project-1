l=[100,200,300,100,200,400,500,100,200]
ind=[]
pos=0
while True:
   print('The List is',l)
   element=int(input("Select an element from the list "))
   print("The Total number of ",element," in the list is ",l.count(element))
   print("Those are in the positions ")
   for i in l:
      ind.append(l.index(element,pos))
      a=l.index(element,pos)
      pos=a+1
   print(ind)