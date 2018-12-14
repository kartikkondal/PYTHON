from threading import Thread
import threading


def DisplayNumbers():
    print("This is the thread [during] the execution of the function ", threading.current_thread().getName()) # To know which thread is working/started
    for count in range(11):
        print(count)
    print("This is the thread [after] the execution of the function  ", threading.current_thread().getName()) # To know which thread is working/started

print("This is the thread [before] the execution of the function ",threading.current_thread().getName()) # To know which thread is working/started
t = Thread(target=DisplayNumbers)

t.start()
