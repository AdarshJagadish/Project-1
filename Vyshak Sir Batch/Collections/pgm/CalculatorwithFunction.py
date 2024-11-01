def add(x,y):
    sum=x+y
    return sum
def sub(x,y):
    sum=x-y
    return sum
def mul(x,y):
    sum=x*y
    return sum
def div(x,y):
    sum=x/y
    return sum
while True:
    print('''
          
*****CALCULATOR*****
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          5. Exit
''')
    ch=int(input("Enter Choice: "))
    if ch>0 and ch<6:        
        a=int(input("Enter 1st Operant: "))
        b=int(input("Enter 2st Operant: "))
        if ch==1:
            s=add(a,b)
            print(s)
        elif ch==2:
            s=sub(a,b)
            print(s)
        elif ch==3:
            s=mul(a,b)
            print(s)
        elif ch==4:
            s=div(a,b)
            print(s)
        elif ch==5:
            break
        else:
            print("Invalid Choice")
    else:
        print("Invalid Choice")