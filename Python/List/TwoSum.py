print("TWO SUM")
li=list()
n=int(input("Enter the number of elements in the list\n"))
print("Enter the elements")
for i in range(n):
    li.append(int(input("\n")))
target=int(input("Enter Target"))
for i in range(len(li)):
    for k in range(len(li)):
        t=li[i]+li[k]
        if i==k:
            continue
        if t==target:
            print(i,k)