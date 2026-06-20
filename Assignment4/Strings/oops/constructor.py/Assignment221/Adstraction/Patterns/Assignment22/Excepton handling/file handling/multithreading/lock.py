'''
# critical section in lock
import threading

count = 0
lock = threading.Lock()

def increment():
    global count
    for i in range(1000):
        lock.acquire()      # lock starts
        count += 1          # CRITICAL SECTION
        lock.release()      # lock ends

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Count:", count)




import threading

balance = 1000
lock = threading.Lock()

def withdraw(amount, name):
    global balance

    lock.acquire()   # enter critical section

    if balance >= amount:
        print(name, "is withdrawing", amount)
        balance -= amount
        print(name, "completed withdrawal. Remaining balance:", balance)
    else:
        print(name, "insufficient balance")

    lock.release()   # exit critical section


t1 = threading.Thread(target=withdraw, args=(700, "Ravi"))
t2 = threading.Thread(target=withdraw, args=(500, "Sita"))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", balance)


#with lock

import threading

balance = 1000
lock = threading.Lock()

def withdraw(amount, name):
    global balance

    with lock:   # automatically acquire and release lock
        if balance >= amount:
            print(name, "is withdrawing", amount)
            balance -= amount
            print(name, "remaining balance:", balance)
        else:
            print(name, "insufficient balance")

t1 = threading.Thread(target=withdraw, args=(700, "Ravi"))
t2 = threading.Thread(target=withdraw, args=(500, "Sita"))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", balance)


'''

import threading

class ATM:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()

    def withdraw(self, amount, name):
        with self.lock:   # critical section protected
            if self.balance >= amount:
                print(name, "is withdrawing", amount)
                self.balance -= amount
                print(name, "remaining balance:", self.balance)
            else:
                print(name, "insufficient balance")
atm = ATM()

t1 = threading.Thread(target=atm.withdraw, args=(700, "Ravi"))
t2 = threading.Thread(target=atm.withdraw, args=(500, "Sita"))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", atm.balance)




