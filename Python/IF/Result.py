print("EXAM RESULT 2024")
n=str(input("Enter Your Full Name\n"))
s=float(input("Enter Your Score\n"))
print(n,"!")
if s<=100 and s>=90:
    print("EXCELLENT\nScore: ",s,"\n Your Grade is A\n You Passed")
elif s<=89 and s>=80:
    print("GOOD\nScore: ",s,"\n Your Grade is B\n You Passed")
elif s<=79 and s>=70:
    print("SATISFACTORY\nScore: ",s,"\n Your Grade is C\n You Passed")
elif s<=69 and s>=60:
    print("NEED IMPROVEMENT\nScore: ",s,"\n Your Grade is D\n You Passed")
elif s<=59 and s>=0:
    print("NEED IMPROVEMENT\nScore: ",s,"\n Your Grade is F\n You Failed")
else :
    print("Please Enter a Valid Score Between 0 to 100")
    