import sqlite3
con=sqlite3.connect('Vyshak Sir Batch/DataBase/Sqlite3/project/details.db')
try:
    con.execute('create table students(s_id int,s_name text)')
except:
    pass
while True:
    print('''
STUDENT MANAGEMENT SYSTEM
    1.Add Student
    2.Update Student          
          ''')
    ch=int(input('Enter a choice: '))
    if ch==1:
        id=int(input('Enter Admission Number: '))
        name=input('Enter student Name: ')
        con.execute('insert into students values(?,?)',(id,name))
        con.commit()
        print('Details Added Successfully')
    elif ch==2:
        id=(int(input("Enter student's id to be updated: ")))
        name=input("Enter new name: ")
        try:
            con.execute('update students set s_name=? where s_id=?',(name,id))
            con.commit()
            print('Details sucessfully Updated')
        except:
            print('Invalid id')
    elif ch==3:
        print('Exited Succesfully')
        break
    else:
        print('Invalid Choice')