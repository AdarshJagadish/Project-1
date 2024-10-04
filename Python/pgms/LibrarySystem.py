user=[{'id': 100, 'name': 'anu', 'email': 'anu@gmail.com', 'phno': '954258625', 'password': 'anu','books':[]}, {'id': 10, 'name': 'amal', 'email': 'amal@gmail.com', 'phno': '964582262', 'password': 'amal','books':[]}]
book=[{'book_id': 100, 'book_name': 'wings of fire', 'stock': 4, 'price': 549}, {'book_id': 101, 'book_name': 'mambazham', 'stock': 2, 'price': 249}]
while True:
    print('''
    1.Register
    2.Login
    3.Exit
    ''')
    ch=int(input('enter choice'))
    if ch==1:
        if len(user)==0:
            id=100
        else:
            id=user[-1]['id']+1
        # print(id)
        name=input('enter name')
        email=input('enter email')
        phno=input('enter phno')
        password=input('enter password')
        user.append({'id':id,'name':name,'email':email,'phno':phno,'password':password})
        # print(user)
    elif ch==2:
        print(user)
        uname=input('enter uname')
        password=input('enter password')
        f=0
        if uname=='admin' and password=='admin':
            print('admin login successfull')
            f=1
            while True:
                print('''
            1.add book
            2.update
            3.delete
            4.view book
            5.view user
            6.logout
            ''')
                sub_ch=int(input('enter ur choice '))
                if sub_ch==1:
                    if len(book)==0:
                        book_id=100
                    else:
                        book_id=book[-1]['book_id']+1
                        # print(id)
                        book_name=input('enter Book Name')
                        stock=int(input('enter available Stock'))
                        price=int(input('enter Price'))
                        book.append({'book_id':book_id,'book_name':book_name,'stock':stock,'price':price})
                        # print(book)
                elif sub_ch==2:
                    id=int(input('enter id'))
                    f1=0
                    for i in book:
                        if i['id']==id:
                            f1=1
                            i['name']=input('enter new name')
                    if f1==0:
                        print('book not available')
                elif sub_ch==3:
                    id=int(input('enter id'))
                    f1=0
                    for i in book:
                        if i['id']==id:
                            f1=1
                            book.remove(i)
                    if f1==0:
                        print('book not available')
                elif sub_ch==4:
                    print('{:<8}{:<25}{:<10}{:<10}'.format('Book ID','Book Name','Stock','Price'))
                    print('-'*0)
                    for i in book:
                        print('{:<8}{:<25}{:<10}{:<10}'.format(i['book_id'],i['book_name'],i['stock'],i['price']))
                elif sub_ch==5:
                    print(user)
                elif sub_ch==6:
                    break
                else:
                    print('invalid choice')                          
        if uname.isdigit():
            uname=int(uname)
        for i in user:
            if i['id']==uname and i['password']==password:
                print('user login successfull')
                f=2
                while True:
                    print('''
            1.View Book
            2.Lend Book
            3.Return Book
            4.Books in Hand
            5.Logout
    ''')
                    sub_ch=int(input("enter coice"))
                    if sub_ch==1:
                        print(book)
                    elif sub_ch==2:
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
                    elif sub_ch==3:
                        id=int(input('enter id'))
                        f1=0
                        for j in book:
                            if j['book_id']==id and id in i['books']:
                                f1=1
                                j['stock']+=1
                                i['books'].remove(id)
                                print('Book Return Successfull')
                        if f1==0:
                            print('book not available')
                    elif sub_ch==4:
                        if len(i['books'])==0:
                            print('no books')
                        else:
                            print(i['books'])
                    elif sub_ch==5:
                        break
                    else:
                        print('invalid choice')
                        
        if f==0:
            print('invalid uname or password')
    elif ch==3:
        break
    else:
        print('invalid choice')