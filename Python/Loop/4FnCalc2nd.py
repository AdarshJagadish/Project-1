print("4 Function Calculator")
c="y"
while (c=="y"):
    print("  1.Addition\n  2.Subtraction\n  3.Multiplication\n  4.Divition\n\n")
    fn=int(input("Choose the corresponding number to perform the function\n"))
    a=int(input("First Number"))
    b=int(input("Second Number"))
    if fn==1:
        r1=a+b
        print(a,"+",b,"=",r1)
    elif fn==2:
        r2=a-b
        print(a,"-",b,"=",r2)
    elif fn==3:
        r3=a*b
        print(a,"*",b,"=",r3)
    elif fn==4:
        r4=a/b 
        print(a,"/",b,"=",r4)
    else:
        print("Wrong Entry")
    print("Do you want to continue?\n")
    c=str(input("y/n\n"))
    if c=="n":
        break
    elif c=="y":
        pass
    else:
        print("Invalid response")