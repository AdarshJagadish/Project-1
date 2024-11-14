class synnefo:
    def python():
        print('Python Training')
class staff(synnefo):
    def staffs():
        print('Staffs')
class student(staff):
    def stud():
        print('Student')
obj=student                            #Can Access synnefo,staff,student classes
obj.python()
obj=staff                              #Can Access synnefo & staff class
obj=synnefo                            #Can Access only synnefo class