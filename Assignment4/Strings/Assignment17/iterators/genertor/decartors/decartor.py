def decorator(func):      # Outer function

    def wrapper():        # Nested function
        print("Before function call")
        func()
        print("After function call")

    return wrapper

@decorator
def greet():
    print("Hello students")

greet()




def decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper
@decorator
def great():
    print("hello student")
greet()

    


decartor in python problem
Python Decorator Problem

A decorator is a function that adds extra functionality to another function without changing its code.

Example Problem 1: Print Before and After Function Call
def my_decorator(func):
    def wrapper():
        print("Function starts")
        func()
        print("Function ends")
    return wrapper

@my_decorator
def greet():
    print("Hello")

greet()

Output:

Function starts
Hello
Function ends
Example Problem 2: Check Login Before Access
def login_required(func):
    def wrapper():
        print("Checking login...")
        func()
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard()

Output:

Checking login...
Welcome to Dashboard
Example Problem 3: Decorator with Arguments
def decorator(func):
    def wrapper(a, b):
        print("Adding numbers")
        result = func(a, b)
        print("Result =", result)
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

add(10, 20)

Output:

Adding numbers
Result = 30
Practice Problem

Create a decorator that prints:

Executing function...

before calling the function.

Expected Output:

Executing function...
Welcome Thanu

Solution:

def show_message(func):
    def wrapper():
        print("Executing function...")
        func()
    return wrapper

@show_message
def welcome():
    print("Welcome Thanu")

welcome()
Interview Definition

Decorator: A decorator is a function that takes another function as input, adds extra functionality, and returns the modified function.

by useing nested function

Yes. Decorators are built using nested functions.

Example: Decorator Using Nested Function
def decorator(func):      # Outer function

    def wrapper():        # Nested function
        print("Before function call")
        func()
        print("After function call")

    return wrapper

@decorator
def greet():
    print("Hello")

greet()

Output:

Before function call
Hello
After function call
How it works
def decorator(func):      # Outer function

    def wrapper():        # Inner/Nested function
        func()

    return wrapper
decorator() → Outer function
wrapper() → Nested (inner) function
return wrapper → Returns the nested function
Without @ Symbol
def decorator(func):

    def wrapper():
        print("Welcome")
        func()

    return wrapper

def hello():
    print("Python")

hello = decorator(hello)

hello()

Output:

Welcome
Python
Practice Problem

Create a decorator that prints "Starting..." before a function and "Completed..." after a function.

def status(func):

    def wrapper():
        print("Starting...")
        func()
        print("Completed...")

    return wrapper

@status
def task():
    print("Task Running")

task()


31. Simple Decorator
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello")

greet()






#2. Welcome Decorator
def welcome(func):
    def wrapper():
        print("Welcome User")
        func()
    return wrapper

@welcome
def display():
    print("Python Learning")

display()




def login_required(func):
    def wrapper():
        print("Checking Login...")
        func()
    return wrapper

@login_required
def dashboard():
    print("Dashboard Opened")

dashboard()
