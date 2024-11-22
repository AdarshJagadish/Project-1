import sqlite3
con=sqlite3.connect('Vyshak Sir Batch/DataBase/Sqlite3/work/std.db')
try:
    con.execute('create table students(st_id int,st_name text,st_email text,st_phno)')
except:
    pass
# con.execute('insert into students values(1,"adarsh","jagadishadarsh@gmail.com",9846675300)')
# con.execute('insert into students values(2,"arunima mohanan","arunima@gmail.com",9846325791)')
# con.execute('insert into students values(3,"abhijith","abhijith@gmail.com",9346395394)')
# con.execute('insert into students values(4,"manu","manu@gmail.com",1589354785)')
# con.execute('insert into students values(5,"adhith","adhi@gmail.com",9546321893)')


data=con.execute('select * from students')
# print('*'*60)
# for i in data:
#     print('{:<4}{:<12}{:<30}{:<12}'.format(i[0],i[1],i[2],i[3]))
# print('*'*60)


# student=con.execute('select * from students where st_id=3')
# print('*'*60)
# for i in student:
#     print('{:<4}{:<12}{:<30}{:<12}'.format(i[0],i[1],i[2],i[3]))
# print('*'*60)

# student=con.execute('select st_name,st_email from students where st_id=3')
# print('*'*60)
# for i in student:
#     print('{:<12}{:<30}'.format(i[0],i[1]))
# print('*'*60)
# con.commit()

# data=con.execute('select count(*) from students')
# for i in data:
#     print(i)

# data=con.execute('select sum(st_id) from students')
# for i in data:
#     print(i)

# data=con.execute('select min(st_id) from students')
# for i in data:
#     print(i)

# data=con.execute('select max(st_id) from students')
# for i in data:
#     print(i)
    
data=con.execute('select avg(st_id) from students')
for i in data:
    print(i)
con.commit() 