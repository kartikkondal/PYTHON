# Using Semaphore is super easy just replace the LOCK object with semaphore
from threading import *


class BookMyBus:
    def __init__(self, SeatsAvailable):
        self.AvailableSeats = SeatsAvailable
        self.l = Semaphore()                                            # This is used for sychronisation

    def buy(self,SeatsRequested):
        self.l.acquire()                                           # This will start the lock


        print("Total Available seats :",self.AvailableSeats)
        if SeatsRequested < self.AvailableSeats:
            print("Confirming a seat ")
            print("Processing the payment ")
            print("Printing the ticket ")
            self.AvailableSeats = self.AvailableSeats - SeatsRequested

        else:

            print("Sorry Housefull no seats available ")
        self.l.release()                                          # This will end the lock of the thread


object = BookMyBus(10)


Customer1 = Thread(target=object.buy,args = (5 ,))

Customer2 = Thread(target=object.buy,args = (4,))

Customer3 = Thread(target=object.buy,args = (1,))


Customer1.start()
Customer2.start()
Customer3.start()




