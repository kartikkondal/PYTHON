from threading import *

class BookMyBus:

    def buy(self):
        print("Confirming a seat ")
        print("Processing the payment ")
        print("Printing the ticket ")






object = BookMyBus()
Customer1 = Thread(target=object.buy)
Customer2 = Thread(target=object.buy)
Customer3 = Thread(target=object.buy)


Customer1.start()
Customer2.start()
Customer3.start()



