c=0
a=int(input("Enter a Number"))
temp=a
while (a>0):
        b=a%10
        c=c*10+b
        a=a//10
        print(c)
        if temp==c:
            print("It is a Palindrome Number")
        else :
            print("not a palindrome")