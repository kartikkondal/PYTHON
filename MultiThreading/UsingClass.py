from threading import *
from time import sleep


class Mythread:
    def displayNumbers(self):
        print(current_thread().getName())
        sleep(1)   # To push into sleep for any number if seconds you want (From time module)

        for count in range(11):
            print(count)


obj = Mythread()

t = Thread(target=obj.displayNumbers)

t.start()

t1 = Thread(target=obj.displayNumbers)

t1.start()

t2 = Thread(target=obj.displayNumbers)

t2.start()

# You can also use it with a single thread and also can use it with creating multiple thread
# In Multple threading you will notice that the output will be very different then the multiple threading and this is due to the
# the Thread schedular of Python which does this