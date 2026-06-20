add the  extra functionality to the without extra function
ex:gift waper extra layer and beauty for it but annot change gift
 validation authentication 
decartors basic function 

#fuctions treated as variables and object also in python





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






def show_args(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@show_args
def student(name, age):
    print(name, age)

student("Thanu", age=20)
