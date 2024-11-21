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

con.execute('update u_detailes set user_phno="9823476159" where user_id=2')
con.commit()