'''
import threading

def student(name, marks):
    print("Student Name:", name)
    print("Marks:", marks)

t1 = threading.Thread(target=student, args=("Tanu", 85))
t2 = threading.Thread(target=student, args=("Ravi", 90))
t3 = threading.Thread(target=student, args=("Sita", 95))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All student details printed") 





import threading
import time

def collect_paper(student_name):
    print("Teacher is collecting paper from:", student_name)
    time.sleep(1)
    print("Paper collected from:", student_name)

students = ["Tanu", "Ravi", "Sita", "Rahul"]

threads = []

for name in students:
    t = threading.Thread(target=collect_paper, args=(name,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All papers collected by teacher")

what is Recognition?

Recognition means identifying or detecting something and understanding what it is.
Why do we use Recognition?

Recognition means identifying or finding something and giving it a name or meaning.

🧠 In simple words:

👉 Recognition = “To identify something correctly”

💻 In Computer Science

We use recognition in many areas:

1. Pattern Recognition
Finding patterns in data
Example: detecting spam emails
2. Face Recognition
Identifying a person using face
Used in mobile unlock (Face ID)
3. Speech Recognition
Converts voice into text
Example: Google Assistant, Siri
4. Object Recognition
Detecting objects in images/videos
Example: self-driving cars
📌 Why we need recognition?
To automate tasks
To reduce human effort
To increase accuracy
To make systems intelligent


def recognize_user(pin):
    if pin == 1234:
        return True
    else:
        return False

def show_balance(balance):
    print("Your Bank Balance is:", balance)

user_pin = int(input("Enter your PIN: "))

if recognize_user(user_pin):
    show_balance(5000)
else:
    print("Invalid PIN. Access Denied")


# ace condition
A race condition happens when two or more threads access and modify the same data at the same time, and the final result depends on the timing of execution.

👉 Because threads run concurrently, the output becomes unpredictable or incorrect.


import threading

balance = 100

def withdraw():
    global balance
    for i in range(10):
        balance -= 10

t1 = threading.Thread(target=withdraw)
t2 = threading.Thread(target=withdraw)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", balance)


# race condition
import threading

count = 0

def increment():
    global count
    for i in range(100000):
        count += 1   # shared data access (problem area)

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Count:", count)


#lock
import threading

count = 0

def add():
    global count
    for i in range(100000):
        count += 1

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Count:", count)

import threading

count = 0

def add():
    global count
    for i in range(1000):
        count += 1

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Count:", count)


# crtical section:
# code rsources access section
import threading

count = 0

def increment():
    global count
    for i in range(1000):
        # Critical Section (shared variable access)
        count += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Count:", count)


import threading

count = 0
lock = threading.Lock()

def add():
    global count
    for i in range(1000):
        lock.acquire()
        count += 1   # critical section
        lock.release()

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Count:", count)

'''