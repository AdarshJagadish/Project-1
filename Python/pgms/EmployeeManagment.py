print('STORE MANAGEMENT SYSTEM')
customer=[{'c_id': 1, 'name': 'adarsh', 'address': 'ayyanthole', 'phno': 9846675300, 'password': 'adarsh'}]
item=[{'i_id': 1, 'i_name': 'pen', 'i_stock': 3, 'i_price': 10.0},{'i_id': 2, 'i_name': 'pencil', 'i_stock': 0, 'i_price': 5.0}]
while True:
    print('''
          1.Register
          2.Login
          3.Exit
        ''')
    opt=int(input('Select an Option: '))
    if opt==1:
        if len(customer)==0:
            c_id=1
        else:
            c_id=customer[-1]['c_id']+1
        name=input('enter name: ')
        address=input('enter address: ')
        phno=int(input('enter phone no: '))
        password=input('enter password: ')
        customer.append({'c_id':c_id,'name':name,'address':address,'phno':phno,'password':password})
        print(customer)
    elif opt==2:
        print('Enter Login Credentials')
        name=input('User name: ')
        password=input('Password: ')
        if name=='admin' and password=='admin123':
            while True:
                print('''
                1. Add Items
                2. Update Stock
                3. Delete Items
                4. View Items
                5. Exit
                ''')
                sub_opt=int(input('Select an Option: '))
                if sub_opt==1:
                    if len(item)==0:
                        i_id=1
                    else:
                        i_id=item[-1]['i_id']+1
                    i_name=input('Enter Item Name: ')
                    i_stock=int(input('No. of Stock: '))
                    i_price=float(input('Enter Price: '))
                    item.append({'i_id':i_id,'i_name':i_name,'i_stock':i_stock,'i_price':i_price})
                    print(item)
                elif sub_opt==2:
                    i_id=(input('Enter Item Id or Item Name'))
                    f1=0
                    for i in item:
                        if i['i_id']==i_id or i['i_name']==i_id:
                            f1=1
                            print(i)
                            i['i_name']=input('Edit Name')
                            if i['i_name']==None:
                                break
                            i['i_stock']=input('Edit stock')
                            if i['i_stock']==None:
                                break
                            i['i_price']=input('Edit Price')
                            if i['i_price']==None:
                                break
                        print(item)
                    if f1==0:
                        print('Item not available')
                elif sub_opt==3:
                    i_id=(input('Enter Item Id or Item Name: '))
                    f1=0
                    for i in item:
                        if i['i_id']==i_id or i['i_name']==i_id:
                            f1=1
                            item.remove(i)
                            print(i['i_name'],' removed from the stock')
                            print('*'*40)
                elif sub_opt==4:
                    print('               Stock List               ')
                    print('*'*40)
                    print('{:<9}{:<10}{:<14}{:<7}'.format('Id','Name','Stock','Price'))
                    print('-'*40)
                    for i in item:
                        print('{:<9}{:<10}{:<14}{:<7}'.format(i['i_id'],i['i_name'],i['i_stock'],i['i_price']))
                        print('-'*40)
                elif sub_opt==5:
                    break
                else:
                    print('Invalid Selection')
        for i in customer:
            if name==i['name'] and password==i['password']:
                sub_opt=int(input('Select an Option: '))
                print('''
                1. View InStock Items
                2. Add to Cart
                3. View Cart
                4. Place Order
                5. Exit''')
                if sub_opt==1:
                    print('          Instock  Item          ')
                    print('*'*31)
                    print('{:<10}{:<14}{:<7}'.format('Name','Stock','Price'))
                    print('-'*31)
                    for i in item:
                        if i['i_stock']>0:
                            print('{:<10}{:<14}{:<7}'.format(i['i_name'],i['i_stock'],i['i_price']))
                            print('-'*31)
                        else:
                            continue
                if sub_opt==1:
                    ji
                if sub_opt==1:
                    ji
                if sub_opt==1:
                    ji
                if sub_opt==5:
                    break
                else:
                    print('Invalid selection')
    elif opt==3:
        break
    else:
        print('Thank You For Visiting')