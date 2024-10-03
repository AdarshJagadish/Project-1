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
        print('{:<8}{:<12}{:<20}{:<10}'.format('roll no','name','email','course'))
        print('-'*50)
        for i in l:
            print('{:<8}{:<12}{:<20}{:<10}'.format(i['roll_no'],i['name'],i['email'],i['course']))
    elif ch==3:
        roll_no=int(input('roll_no'))
        f=0
        for i in l:
            if i['roll_no']==roll_no:
                print('''
1. Name
2.Email
3.Course
                    ''')
                o=int(input())
                if o==1:
                    name=str(input('new name '))
                    i['name']=name
                    f=1
                elif o==2:
                    email=str(input('new email '))
                    i['email']=email
                    f=1
                elif o==3:
                    course=str(input('Course '))
                    i['course']=course
                    f=1
                else:
                    break
        if f==0:
            print('id not available')
    elif ch==4:
        roll_no=int(input("enter roll_no"))
        f=0
        for i in l:
            if i['roll_no']==roll_no:
                l.remove(i)
                f=1
        if f==0:
            print('not a valid roll_no')
    elif ch==5:
        break
    else:
        print('Invalid choice')