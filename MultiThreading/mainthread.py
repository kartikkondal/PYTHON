import threading
print("The Current Thread that is running :",threading.current_thread().getName())


if threading.current_thread() == threading.main_thread():
    print("Main Thread running ")