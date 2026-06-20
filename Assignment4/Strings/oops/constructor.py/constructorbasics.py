#why use a constructor?
#to unitialize object data when the object is created


class Car:
    def __init__(self, brand):
        self.brand= brand
c1 = Car("toyota")
print(c1.brand)


#___init__ is a constructor





class Bank:
    def __init__(self, balance):
        self.balance = balance
b1 = Bank("500")   
print(b1.balance)




#balance = parameter
#self.balance=instanes variable



    #it is special method in python it is  automatical called when object is created
    # why we can use?
    #
       
    
class Student:
    def __init__(self, name):
        self.Name = name
s1 = Student("gani")   
print(s1.name)  


#types ofconstructor
#default constructor
#parameterized constructor
#constructor with parameters





#static
#all instances of class



#self means current objectlocation will be give




#destructor
#when constructor gets called?
#destructors are called when objects gets destroyed,simple
#end of the program
#def keyword
#lets add destructor
#__del__()


#inheritance
#cclass className(parentClass




#class CopperBottle(Bottle):
    #def




class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Tanu", 20)
s1.show()   





#self points to object
#after intialize the variables
#self is a current variable
#sef.name is current variabl stored




#defaultconstructor

class Student:
    def __init__(self):
        print("Default Constructor Called")

s1 = Student()




#automatical called when we can create a bject
#fixed name-__init-__
#bormal method
#we can call
#they have no fixed name
#self is conversion

#what is a use of self?
#it is current variable


#instances variables
# they store object specific data
# the things are dife     



class Student:
    def __init__(self):
        self.name = "Tanu"
        self.age = 20

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student()
s1.display()



#Tanu, here are some Instance Variable-based Python OOP problems often asked in interviews and coding rounds.
##1. Student Class

#Create a class Student with instance variables:

#name
#age
#marks

#Print student details.



class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

s1 = Student("Rahul", 21, 85)
s1.display()




#Instance Method in Python
#An instance method is a method that works with instance variables and uses the self parameter.

class Student:
    def __init__(self, name):
        self.name = name

    def display(self):      # Instance Method
        print("Name:", self.name)


#tell me the internal work of instances method

#class varible
#self
#self refers to current object




class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Instance Method
    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

# Creating Objects
s1 = Student("Tanu", 90)
s2 = Student("Rahul", 85)

# Calling Instance Method
s1.show()
s2.show()











#method over riding


