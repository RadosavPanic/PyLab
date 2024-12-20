from threading import *
import threading
from time import sleep

lock = threading.Lock()


class FirstThread(Thread):
    def run(self):
        for i in range(3):
            lock.acquire()
            print("Lock acquired")
            print("First thread operation")
            sleep(1)
            lock.release()


class SecondThread(Thread):
    def run(self):
        for i in range(3):
            lock.acquire()
            print("Lock acquired")
            print("Second thread operation")
            sleep(1)
            lock.release()


firstThread = FirstThread()
secondThread = SecondThread()
firstThread.start()
sleep(0.1)
secondThread.start()