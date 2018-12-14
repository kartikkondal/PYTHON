from threading import *


class BookMyBus:
    def __init__(self, SeatsAvailable):
        self.AvailableSeats = SeatsAvailable
        self.l = Lock()                                            # This is used for sychronisation

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

'''
Sychronisation is used to synchronise the threads so that they can work properly 
we can see in the above example that there will be some cases when the thread will posoon the deduction of the seats and thus there will be seats available even 
afer the reduction of the seats and thats because the reduction never happend 
so to sychronize this process we use LOCK



'''


