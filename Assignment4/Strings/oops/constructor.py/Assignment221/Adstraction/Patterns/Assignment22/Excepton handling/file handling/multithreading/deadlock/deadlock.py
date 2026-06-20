'''
Deadlock in Python (Threading)

A deadlock happens when two or more threads are waiting forever for each other to release locks, so the program gets stuck and never continues.

It usually occurs in multithreading programs when we use multiple locks.

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    lock1.acquire()
    print("Task1 locked lock1")

    time.sleep(1)

    lock2.acquire()
    print("Task1 locked lock2")

    lock2.release()
    lock1.release()

def task2():
    lock2.acquire()
    print("Task2 locked lock2")

    time.sleep(1)

    lock1.acquire()
    print("Task2 locked lock1")

    lock1.release()
    lock2.release()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()


deadlock, r lock,


'''

