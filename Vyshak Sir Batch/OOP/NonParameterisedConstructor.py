class synnefo:
    def __init__(self):
        self.name=input('Enter Name: ')
        self.age=int(input('Enter age: '))
        self.place=input('Enter your place: ')
    def python(self):
        print(self.name,self.age,self.place)
    def php(self):
        print(self.name,self.age,self.place)
std1=synnefo()
std1.python()
std1.php()