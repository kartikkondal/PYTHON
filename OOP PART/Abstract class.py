from abc import abstractmethod,ABC
class shape(ABC):

    @abstractmethod
    def Area(self):
        pass

class rect(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def Area(self):
        print("the Area of the Rectangle is ",self.l*self.b)

class square(shape):
    def __init__(self,side):
        self.side = side

    def Area(self):
        print("The Area of the Square is ",self.side*self.side)

s = square(2)
s.Area()
