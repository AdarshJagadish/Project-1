l=[100,200,300,100,200,400,500,100,200]
indx=0
ind=[]
while True:
   print('The List is',l)
   element=int(input("Select an element from the list "))
   print("The Total number of ",element," in the list is ",l.count(element))
   print("Those are in the positions ")
   for i in l:
      x=l.index(element,indx)
      if x in ind:
         pass
      else:
         ind.append(x)
         indx=x+1
   print(ind)