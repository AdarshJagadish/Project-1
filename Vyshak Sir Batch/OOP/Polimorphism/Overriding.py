class novavi:
    def staff(self):
        print('Novavi Staff')
class synnefo(novavi):
    def staff(self):
        super().staff()
        print('Synnefo Staff')
obj=synnefo()
obj.staff()