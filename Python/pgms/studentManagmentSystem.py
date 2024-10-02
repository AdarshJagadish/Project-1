l=[{'roll_no': 1,'name': 'adarsh','email':'fhagag@kd.com','course':'Bsc IT'}]
while True:
    print('''
1.Add std
2.View std
3.Update std
4.Delete std
5.Exit
          ''')
    ch=int(input('choice: '))
    if ch==1:
        roll_no=int(input('roll no '))
        name=str(input('name '))
        email=str(input('email '))
        course=str(input('course '))
        l.append({'roll_no':roll_no,'name':name,'email':email,'course':course,})
    elif ch==2:
        print('{:<8}{:<12}{:<20}{:<10}'.format('roll no','Name','Name','Email','course'))
        print('-'*50)
        for i in l:
            print('{:<8}{:<12}{:<20}{:<10}'.format(i['roll_no'],i['name'],i['email'],i['course']))
    # elif ch==3:
        
    # elif ch==4:
    #     a=int(input('no1: '))
    #     b=int(input('no2: '))
    #     print(a/b)
    # elif ch==5:
    #     break
    else:
        print('Invalid choice')