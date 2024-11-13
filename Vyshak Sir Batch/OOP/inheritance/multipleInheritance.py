class school:
    def teacher():
        print('Teacher')
class tution:
    def notes():
        print('Notes')
class student(school,tution):
    def learning():
        print('Learning')
user=student                    #Can access each fn()s from both 3 class
user1=tution                    #Can only access tution class fn()s
user2=school                    #Can only access school class fn()s
user.teacher()
user.notes()
user1.notes()