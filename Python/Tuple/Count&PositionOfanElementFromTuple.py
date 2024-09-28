tuple=(12,52,85,25,2,3,85,3,25,65,3,2,5,9,3,1,2,5,1,3,5,2)
n=int(input("Enter the number to be find the count and positions  "))
print("There is",tuple.count(n))
pos=0
count=tuple.count(n)
while count>0:
    p=tuple.index(n,pos)
    print(p)
    pos=p+1
    count-=1
