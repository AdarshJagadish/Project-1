print('STORE MANAGEMENT SYSTEM')
customer=[{'c_id': 1, 'name': 'adarsh', 'address': 'ayyanthole', 'phno': 9846675300, 'password': 'adarsh'}]
item=[]
while True:
    print('''
          1.Register
          2.Login
          3.Exit
        ''')
    opt=int(input('Select an Option'))
    if opt==1:
        if len(customer)==0:
            c_id=1
        else:
            c_id=customer[-1]['id']+1
        name=input('enter name: ')
        address=input('enter address: ')
        phno=int(input('enter phone no: '))
        password=input('enter password: ')
        customer.append({'c_id':c_id,'name':name,'address':address,'phno':phno,'password':password})
        print(customer)
    elif opt==2:
        'fdfdy'
    elif opt==3:
        break
    else:
        print('Thank You For Visiting')