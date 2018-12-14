from threading import *
from time import *

class Producer:     # This class is reponsible for producing the products

    def __init__(self):
        self.Product = []
        self.OrdersPlaced = False

    def produce(self):
        for count in range(1,5):
            self.Product.append("Product"+str(count))
            sleep(1)
            print("Item added")

        self.OrdersPlaced = True


class Consumer:
    def __init__(self,prod):
        self.prod = prod

    def consume(self):
        while self.prod.OrdersPlaced == False:
            sleep(0.2)
        print("Orders shipped ",self.prod.Product)


p = Producer()

c = Consumer(p)

t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

t1.start()

t2.start()




