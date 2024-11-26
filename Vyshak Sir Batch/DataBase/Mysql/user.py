import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='user',
    password='user123',
    database='sample'
)
mycursor=mydb.cursor()
try:
    mycursor.execute('create database sample')
except:
    pass
# mycursor.execute('Create table student(admno int,name text,email text)')
lt=int(input('Enter limit'))
for i in range(lt):
    adno=int(input('admission number: '))
    name=input('name: ')
    email=input('email: ')
    mycursor.execute('insert into student values(%s,%s,%s)',(adno,name,email))
    
mydb.commit()