students=[]
limit=int(input('Number of Entrys'))
for i in range(1,limit+1):
    print('Student :',i)
    sname=input("Enter name of the student : ")
    sage=input("Enter age of the student : ")
    splace=input("Enter place of the student : ")
    students.append({'name':sname,'age':sage, 'place':splace})
print(students)