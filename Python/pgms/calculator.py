while True:
    print('''
1.Add
2.Sub
3.Mul
4.Div
5.Mod
6.Exit
          ''')
    ch=int(input('choice: '))
    if ch==1:
        a=int(input('no1: '))
        b=int(input('no2: '))
        print(a+b)
    elif ch==2:
        a=int(input('no1: '))
        b=int(input('no2: '))
        print(a-b)
    elif ch==3:
        a=int(input('no1: '))
        b=int(input('no2: '))
        print(a*b)
    elif ch==4:
        a=int(input('no1: '))
        b=int(input('no2: '))
        print(a/b)
    elif ch==5:
        a=int(input('no1: '))
        b=int(input('no2: '))
        print(a%b)
    elif ch==6:
        break
    else:
        print('Invalid choice')