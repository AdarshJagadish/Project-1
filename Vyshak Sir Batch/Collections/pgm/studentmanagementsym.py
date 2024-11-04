students=[{'Admission Number': '1', 'Student Name': 'Shyam', 'Student Age': 21, 'Course Name': 'MD'},{'Admission Number': '2', 'Student Name': 'anu', 'Student Age': 21, 'Course Name': 'MBBS'}]
while True:
    print('''
******STUDENT MANAGEMENT SYSTEM******

1. Add Student
2. Delete Student
3. Search Student
4. Show All Students
5. Exit
''')
    try:
        ch=int(input('Enter a Choice: '))
    except:
        print('AN Error Occured')
    if ch==1:
        print('*****ADD STUDENT*****')
        limit=int(input('Number of Students to be Added: '))
        if limit>0:
            for i in range(limit):
                print('Enter Student ',i+1)
                admno=int(input('Enter Student Admission Number: '))
                stname=input('Enter Name: ')
                stage=int(input('Enter Student Age: '))
                stcourse=input('Enter Course Name: ')
                students.append({'Admission Number':admno,'Student Name':stname,'Student Age':stage,'Course Name':stcourse,})
                print(students)
    elif ch==2:
        print('*****DELETE STUDENT*****')
        did=input('Enter Admission Number to Delete Student: ')
        flag=0
        for i in students:
            if i['Admission Number']==did:
                students.remove(i)
                flag=1
                print(students)
        if flag==0:
                print('id not found')
    elif ch==3:
        print('*****SEARCH STUDENT*****')
        id=int(input('Enter Student Id to search: '))
        flag=0
        for i in students:
            if i['Admission Number']==id:
                print(i)
                flag=1
        if flag==0:
                print('id not found')
    elif ch==4:
        print('*****SHOW ALL STUDENTS*****')
        print(students)
    elif ch==5:
        print('*****EXIT*****')
        break
    else:
        print('INVALID OPTION')