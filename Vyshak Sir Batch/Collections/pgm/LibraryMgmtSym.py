library=[{'Id': '1', 'Name': 'gsegge', 'Author': 'efsdg', 'Stock': 2}]
while True:
    print('''
********LIBRARY MANAGEMENT SYSTEM********
          
1. Add book
2. Update book
3. Remove book
4. View All books
5. Search book
6. Exit
          ''')
    ch=int(input('Select an Option: '))
    if ch==1:
        b_id=input('Enter Book ID: ')
        b_name=input('Enter Name: ')
        b_author=input('Enter Author Name: ')
        b_stock=int(input('Enter No of Stock to be added: '))
        library.append({'Id':b_id,'Name':b_name,'Author':b_author,'Stock':b_stock})
        print('Book Added Succesfully!!')
        print('''
*************BOOK LIST*************
              ''')
        print('{:<4}{:<12}{:<12}{:<7}'.format('ID','Name','Author','Stock'))
        print('*'*35)
        for i in library:
            print('{:<4}{:<12}{:<12}{:<7}'.format(i['Id'],i['Name'],i['Author'],i['Stock']))
    elif ch==2:
        b_id=input('Enter the book id to be modified: ')
        for i in library:
            if b_id==i['Id']:
                print('*'*35)
                print('{:<4}{:<12}{:<12}{:<7}'.format(i['Id'],i['Name'],i['Author'],i['Stock']))
                print('*'*35)
                while True:
                        
                    subch=int(input('''
What do you want to modify??
                                    
1. ID
2. Name
3. Author
4. Stock
5. Exit
        
    '''))
                    if subch==1:
                        for i in library:
                            if b_id==i['Id']:
                                nid=input("Enter New Id: ")
                                i['Id']=nid
                                print('*'*35)
                                print('{:<4}{:<12}{:<12}{:<7}'.format(i['Id'],i['Name'],i['Author'],i['Stock']))
                                print('*'*35)
                    elif subch==2:
                        for i in library:
                            if b_id==i['Id']:
                                nname=input("Enter New Name: ")
                                i['Name']=nname
                                print('*'*35)
                                print('{:<4}{:<12}{:<12}{:<7}'.format(i['Id'],i['Name'],i['Author'],i['Stock']))
                                print('*'*35)
                    elif subch==3:
                        for i in library:
                            if b_id==i['Id']:
                                nauthor=input("Enter New Author Name: ")
                                i['Author']=nauthor
                                print('*'*35)
                                print('{:<4}{:<12}{:<12}{:<7}'.format(i['Id'],i['Name'],i['Author'],i['Stock']))
                                print('*'*35)
                    elif subch==4:
                        for i in library:
                            if b_id==i['Id']:
                                nstk=input("Enter New Stock: ")
                                i['Stock']=nstk
                                print('*'*35)
                                print('{:<4}{:<12}{:<12}{:<7}'.format(i['Id'],i['Name'],i['Author'],i['Stock']))
                                print('*'*35)
                    elif subch==5:
                        break
                    else:
                        print('Invalid Choice')
                    print('Details Updated Succesfully!!')
    elif ch==3:
        b_id=input('Enter the book id to be Removed: ')
        for i in library:
            if b_id==i['Id']:
                library.remove(i)
        print('Book Removed Succesfully!!')
    elif ch==4:
        print('''******BOOK LIST******
              ''')
        print('{:<4}{:<12}{:<12}{:<7}'.format('ID','Name','Author','Stock'))
        print('*'*35)
        for i in library:
            print('{:<4}{:<12}{:<12}{:<7}'.format(i['Id'],i['Name'],i['Author'],i['Stock']))
        print('*'*35)
    elif ch==5:
        b_id=input('Enter the Id or Name to Search: ')
        for i in library:
            if b_id==i['Id'] or b_id==i['Name']:
                print('''Book Found!!
                      ''')
                print('{:<4}{:<12}{:<12}{:<7}'.format(i['Id'],i['Name'],i['Author'],i['Stock']))
    elif ch==6:
        break
    else:
        print('Not a Valid Option')