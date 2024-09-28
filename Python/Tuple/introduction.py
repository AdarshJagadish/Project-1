# tuple is immutable ,differ from list
# output of a single element will be the element data type without bracket()          eg: if t=(10,) print(t)       i/o: 10 

t=(1,5,2,3,5)                        # tuple difine with cirular bracket ()
t=(1,)                               # for single elemnt tuple ,should use a , after the element
t=0,2,5,5                            # also consider as a tuple,default data type tuple when use comma without bracket
t=(1,[10,11],2)                      # a tuple with a list inside     can change list even though it in inside a tuple    eg:t[1].apped(12)



# methods
# index- t.index()               -To find the index position of an element
# count_ t.count()               -To find the count of an element
