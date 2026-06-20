#polymorphism
#Polymorphism Definition

#Polymorphism is an OOP concept where the same method or function can perform different actions depending on the object that calls it
#same operator but different behaviour

#types of polymprphism
#compile time
#run time
#complie time polymorphism t can hlp in methd overloading
#no method overloading in python
#ethod Overloading means having multiple methods with the same name but different parameters.
#not directly possible in python
#but it can use varible length arguments
#example;
class Demo:
    def add(self, a, b=0, c=0):
        print(a + b + c)

d = Demo()

d.add(10)          # 10
d.add(10, 20)      # 30
d.add(10, 20, 30)  # 60


#run time polymorphism
#it can based on overriding

#in overiding same methods but diff variables
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Dog()
a.sound()

a = Cat()
a.sound()



class Bird:
    def fly(self):
        print("Bird can fly")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies high in the sky")

b = Eagle()
b.fly()




class Bird:
    def fly(self):
        print("Bird can fly")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies high in the sky")

b = Eagle()
b.fly()




class Bird:
    def fly(self):
        print("Bird can fly")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies high in the sky")

b = Eagle()
b.fly()



class Duck:
    def sound(self):
        print("Duck says Quack")

class Dog:
    def sound(self):
        print("Dog says Bark")

animals = [Duck(), Dog()]

for a in animals:
    a.sound()



