from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def tyre():
        print('tyre')
class bike(vehicle):
    def tyre():
        pass
    def color():
        print('Red')
obj=bike
obj.color()