book=[]
user=[]
def reg():
    if len(user)==0:
        id=100
    else:
        id=user[-1]['id']+1
    name=input('Enter your name: ')
    age=int(input('Enter your age: '))
    place=input('Enter your place: ')
    ph=int(input('Enter phone nuimber: '))
    password=(input('Enter password: '))
    user.append({'id':id,'name':name,'age':age,'place':place,'ph':ph,'password':password})
def login():
    username=input('Enter your User Id Here: ')
    password=(input('Enter the password: '))
    f=0
    if username=='admin' and password=='admin123':
        f=1
    if username.isdigit():
        username=int(username)
        for i in user:
            if i['id']==username and i['password']==password:
                f=2
                users=i
    if f==0:
        print('invalid username or password')
    return f
    return users
def add_book():
    if len(book)==0:
        book_id=100
    else:
        book_id=book[-1]['book_id']+1
        book_name=input('enter Book Name')
        stock=int(input('enter available Stock'))
        price=float(input('enter Price'))
        book.append({'book_id':book_id,'book_name':book_name,'stock':stock,'price':price})
        print(book)
def view_book():
    print('{:<8}{:<25}{:<10}{:<10}'.format('Book ID','Book Name','Stock','Price'))
    print('-'*40)
    for i in book:
        print('{:<8}{:<25}{:<10}{:<10}'.format(i['book_id'],i['book_name'],i['stock'],i['price']))
def update():
    id=int(input('enter id'))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            i['name']=input('enter new name')
            if f1==0:
                print('book not available')
def delete():
    id=int(input('enter id'))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            book.remove(i)
        if f1==0:
            print('book not available')
def view_user():
    print('{:<8}{:<25}{:<4}{:<15}{:<10}'.format('User ID','Name','Age','Place','Phone No.'))
    print('-'*40)
    for i in book:
        print('{:<8}{:<25}{:<4}{:<15}{:<10}'.format(i['id'],i['name'],i['age'],i['place','ph']))
def lend_book():
    id=int(input('enter id'))
    f1=0
    for j in book:
        if j['book_id']==id:
            f1=1
            if j['stock']>0:
                i['books'].append(id)
                j['stock']-=1
            else:
                print('out of stock')
            if f1==0:
                print('book not available')
def return_book():
    id=int(input('enter id'))
    f1=0
    for j in book:
        if j['book_id']==id and id in i['books']:
            f1=1
            i['stock']+=1
            i['books'].remove(id)
            print('Book Return Successfull')
        if f1==0:
            print('book not available')
def book_taken():
    if len(i['books'])==0:
        print('no books')
    else:
        print(i['books'])
def view_profile():
    print(i['user'])

while True:
    print('''
    1.Register
    2.Login
    3.Exit
    ''')
    ch=int(input('Choose an Option'))
    if ch==1:
        reg()
    elif ch==2:
        f=login()
        if f==1:
            print('admin login successfull')
            while True:
                print('''
            1.add book
            2.view book
            3.update
            4.delete
            5.view user
            6.logout
            ''')
                ch=int(input('choose an option'))
                if ch==1:
                    add_book()
                elif ch==2:
                    view_book()
                elif ch==3:
                    update()
                elif ch==4:
                    delete()
                elif ch==5:
                    view_user()
                elif ch==6:
                    break
                else:
                    print('invalid option')
        elif f==2:
            print('login sucessfull')
            while True:
                print('''
            1.View Book
            2.Lend Book
            3.Return Book
            4.Books in Hand
            5.Logout
            ''')
            ch=int(input('choose an option'))
            if ch==1:
                view_book()
            elif ch==2:
                lend_book()
            elif ch==3:
                return_book()
            elif ch==4:
                book_taken()
            elif ch==5:
                view_profile()
            elif ch==6:
                break
            else:
                print('invalid option')
    elif 3:
        break
    else:
        print('Invalid')