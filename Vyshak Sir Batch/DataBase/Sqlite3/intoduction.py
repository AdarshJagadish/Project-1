import sqlite3
con=sqlite3.connect('Vyshak Sir Batch/DataBase/Sqlite3/user.db')
try:
    con.execute('create table u_detailes(user_id int,user_name text,user_email text,user_phno int)')
except:
    pass
# limit=int(input('Enter the limit: '))
# for i in range(limit):
#     id=int(input('Enter user id: '))
#     name=input('Enter user name: ')
#     email=input('Enter user email: ')
#     phno=int(input('Enter user phno: '))
    # con.execute('insert into u_detailes values(?,?,?,?)',(id,name,email,phno))

# con.execute('update u_detailes set user_phno="9823476159" where user_id=2')

# con.execute('delete from u_detailes where user_id=2')



# data=con.execute('select * from u_detailes')
# for i in data:
#     print('*'*60)
#     print('{:<4}{:<12}{:<30}{:<12}'.format(i[0],i[1],i[2],i[3]))
#     print('*'*60)

data=con.execute('select count(*) from u_detailes')
for i in data:
    print(i)
con.commit()