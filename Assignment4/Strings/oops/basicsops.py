types of oops
OOP has 4 pillars:

#Encapsulation
#Inheritance
#Polymorphism
#Abstractio



why use oops in python?
where the program organize used class and object
object cantains two types
variables 
behaviour
in oops can callfunction in methods
propertices references to variables
actions refer to methods
earlier program return to oops
it is very diffcult to larger program
when comeing with out 
major propertices
less securiy diffcult maintances
intrduceing oops concepts
classes
object
encapusaulation#security purpose
inheritance#parent and child
abstraction#hiding the implementaion
polyermerfisum#man form of singal intenity



#class
class is a collectionof variables and methods
                   or
bule print of object



#class strt with capital letter
#it is keyword it create calss name
class is a identifier
pass


#object is instances of class
actual memory representation of class
        



class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


# Creating objects
s1 = Student("Tanu", 21, 95)
s2 = Student("Ravi", 22, 88)

s1.display()
print("------")
s2.display()        




class Student:
    pass

s = Student()
print(s)




class Car:
    brand = "Ode"
c1 = Car()

print(c1.brand)
print(c1.color)
print(Car.brand)


#self is  keyword  it refres to current object
#creates a object



class Car:
    brand = "Toyota"
    color = "White"

    def drive(self):
        print("Car is driving")


# Object creation
c1 = Car()

print(c1.brand)
print(c1.color)

c1.drive()




class Employee:
    name(employee) = "tanuja"
    companyname = "tcs"
    self.name()
    start
e1 = Employee()
print(e1.company)



   