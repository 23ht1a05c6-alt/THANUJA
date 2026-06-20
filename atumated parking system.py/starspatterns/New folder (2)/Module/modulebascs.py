'''
What is a Module?

A module is a file containing Python code (functions, variables, classes) that can be reused in another Python program.




def add(a, b):
    return a + b

def sub(a, b):
    return a - b



def add(a, b):
    return a + b


import calculator

print(calculator.add(10, 20))

1. Built-in Modules

Python provides these modules by default.

Examples:

math
random
datetime
os
'''


import math

print(math.sqrt(25))
print(math.factorial(5))




#
import random

print(random.randint(1, 10))



#datetime Module
import datetime

print(datetime.datetime.now())


#4. os Module
import os

print(os.getcwd())


from datetime import date

birth_year = int(input("Enter Birth Year: "))
birth_month = int(input("Enter Birth Month: "))
birth_day = int(input("Enter Birth Day: "))

today = date.today()
birth_date = date(birth_year, birth_month, birth_day)

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Age =", age)




for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")



        