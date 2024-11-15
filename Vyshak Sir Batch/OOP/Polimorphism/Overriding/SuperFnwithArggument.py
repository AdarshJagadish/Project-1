class school:
    def __init__(self,sname):
        print(sname)
class student(school):
    def __init__(self,sname,slocation):
        super().__init__(sname)
        print(slocation)
obj=student('JMC','Thrissur')