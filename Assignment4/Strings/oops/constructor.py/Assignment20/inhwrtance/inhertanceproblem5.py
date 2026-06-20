#method overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):   # Overriding parent method
        print("Dog barks")

d = Dog()
d.sound()


#super funtion()
#super() Function in Python

#super() is used to call a method from the parent class inside the child class.
#example;
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()   # Call parent class method
        print("Dog barks")

d = Dog()
d.sound()


#example2:
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, rollno):
        Person.__init__(self, name)  # Parent constructor
        self.rollno = rollno

s = Student("Tanu", 101)
print(s.name)
print(s.rollno)



class Parent:
    def __init__(self):
        print("parent constructor")
class Child(Parent):
    def __init__(self):
        print("child constructor")
c1 = Child ()



#super()in constructor
class Person:
    def __init__(self, name):
        self.name = name
        print("Parent Constructor")

class Student(Person):
    def __init__(self, name, rollno):
        super().__init__(name)   # Calls Parent Constructor
        self.rollno = rollno
        print("Child Constructor")

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)

s = Student("Tanu", 101)
s.display()



#important
#MRO:
#method resolution order(revalution can speak it in resolution)
#python searchs methods order


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

d1 = D()
d1.show()
print(D.mro())



