import sqlite3
con=sqlite3.connect('Vyshak Sir Batch/DataBase/Sqlite3/work/student2/studentdetails.db')
try:
    con.execute('create table students(id int,name text,email text,mark int)')
except:
    pass
# limit=int(input('Enter Limit: '))
# for i in range(limit):
    # print('Student',i+1)
    # id=i+1
    # name=input('NAME: ')
    # email=input('EMAIL: ')
    # mark=int(input('MARK: '))
    # con.execute('insert into students values(?,?,?,?)',(id,name,email,mark))
    
# id=int(input('Enter id: '))
# name=input('Enter new name: ')
# con.execute('update students set name=? where id=?',(name,id))
max=con.execute('select max(mark) from students')
for i in max:
    for j in i:
        print('Maximum Mark is ',j)
min=con.execute('select min(mark) from students')
for i in min:
    for j in i:
        print('Minimum Mark is ',j)
avg=con.execute('select avg(mark) from students')
for i in avg:
    for j in i:
        print('Average Mark is ',j)
sum=con.execute('select sum(mark) from students')
for i in sum:
    for j in i:
        print('Total Mark is ',j)
count=con.execute('select count(mark) from students')
for i in count:
    for j in i:
        print('Total Count of Mark is ',j)
con.commit()
