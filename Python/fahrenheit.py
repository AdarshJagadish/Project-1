print('TEMPERATURE CALCULATOR\n')
print('1.C to F\n2.F to C\n3.C to K\n4.F to K\n5.K to F\n6.K to C\n')
op=int(input('Select an Option from Above\n'))
t=float(input("Enter the temperature to be converted\n"))
if op==1:
    r=t*(9/5)+32
    print(r,"F")
elif op==2:
    r=(t-32)*5/9
    print(r,"C")
elif op==3:
    r=t+273.15
    print(r,"K")
elif op==4:
    r=(t-32)*5/9+273.15
    print(r,"K")
elif op==5:
    r=(t-273.15)*(9/5)+32
    print(r,"F")
elif op==6:
    r=t-273.15
    print(r,"C")
else:
    print("Select a Valid Option")