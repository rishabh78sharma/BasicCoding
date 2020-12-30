from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length=4
        self.breath=4

    def printarea(self):
        print(f'Area is {self.lengthcod* self.breath}')


harry=Rectangle()
harry.printarea()