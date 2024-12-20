from threading import *
from time import sleep


class GreetOne(Thread):
    def run(self):
        for i in range(5):
            print("Hello from first class")
            sleep(1)


class GreetTwo(Thread):
    def run(self):
        for i in range(5):
            print("Hello from second class")
            sleep(1)


firstThread = GreetOne()
secondThread = GreetTwo()
firstThread.start()
sleep(0.1)
secondThread.start()
# main thread will wait for both threads to finish execution to continue with process, because of join() method
firstThread.join()
secondThread.join()
print("End of program")
