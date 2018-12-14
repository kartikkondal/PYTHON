# In this case we are inheriting a sub class from the class Thread and
# we are overiding a function called run in it which has the same
# functionality that we want



from threading import Thread


class Mythread(Thread):
    def run(self):
        for count in range(11):
            print(count)


t = Mythread()
t.start()  # It will spawn off a new Thread internally and run the overiden function

#  Remember!!!! don't invoke the function manually as it will start the Main thread and the new Thread will not be spawned off

