#todo check + operator for lists
#todo check + operator for objects

class First:
    def __init__(self,Number1,Number2):
        self.a = Number1
        self.b = Number2


    def show(self):
        print(self.a,self.b)
    def operator_

class Second:
    def __init__(self,c,d):
        self.c = c
        self.d = d

    def show(self):
        print(self.c,self.d)


f = First(1,1)
b = Second(1,1)

f = f+b
f.show()
