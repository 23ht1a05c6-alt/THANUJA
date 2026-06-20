#it is a mechanium wherer one 
#one class reuses the features of another class
#use variables
#use methods
#with rewriteing the code again
#Definition:
#Inheritance is an OOP concept where one class (child class) acquires 
# the properties and methods of another class (parent class).
#write code once use number of times the reuseability of code



#benfits:
#Code reusability
#Easy maintenance
#Supports method overriding
#Reduces duplicate code

#terms:
#parent(super class)
#child(sub class)

#syntax:
class Parent:
    # Parent class members
    pass

class Child(Parent):
    # Child class members
    pass





# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child Class
class Dog(Animal):
    def eating(self):
        print("animal is eating")

# Object Creation
d = Dog()

d.sound()   # Inherited method
d.eating()    # Child method




#singal inertance
#mulitple inhertance
#hierachical inhertance
#hybrid inhertnce


#singal inhertance
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()   # Inherited from Animal
d.bark()    # Dog's own method



#multiple inhertane
#Definition:
#Multiple Inheritance is a type of inheritance where one 
# child class inherits from more than one parent class.
#syntax:
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass


class Father:
    def father_property(self):
        print("Father's Property")

class Mother:
    def mother_property(self):
        print("Mother's Property")

class Child(Father, Mother):
    def child_property(self):
        print("Child's Property")

c = Child()

c.father_property()
c.mother_property()
c.child_property()



#multiple level of inhertance
#Multilevel Inheritance is a type of inheritance 
# where one class inherits from another class, and then a third class inherits from the second class.
# grandparent

#parent
#son
#example:

class Grandparent:
    def house(self):
        print("Grandparent has a house")

class Parent(Grandparent):
    def car(self):
        print("Parent has a car")

class Child(Parent):
    def bike(self):
        print("Child has a bike")

c = Child()

c.house()
c.car()
c.bike()


#hybrid inhertance
#Hybrid Inheritance is a combination of two or more types of inheritance (such as single, multiple, and multilevel inheritance) in one program.

#Definition

#Hybrid Inheritance combines different inheritance types to form a more complex inheritance structure
#diagram:
      #Grandfather
         #  ↓
        #Father
         #  ↓
         #Son
         #  ↑
        #Mother



class Father:
    def father_property(self):
        print("Father's Property")

class Mother:
    def mother_property(self):
        print("Mother's Property")

class Son(Father, Mother):
    def son_property(self):
        print("Son's Property")

s = Son()

s.father_property()
s.mother_property()
s.son_property()   



#is sub class;
#we can two class child class
#parent class

class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))

#instances class
class Student:
    def display(self):
        print("Hello Student")

s1 = Student()   # Instance/Object
s2 = Student()   # Another Instance/Object

s1.display()
s2.display()




class Student:
    pass

s = Student()

print(isinstance(s, Student))


#create animal with sound that shold print animl makeAnimal

# create object as a call




# Parent Class
class College:
    
        print("College name is city")

# Child Class
class Student(College):
    def name(self):
        print("student name is tanuja")

# Object Creation
s = Student()

s.name()   # Inherited method
 

#problem3;
#mult levelinhertance
#vechile classwit method class
#follwed  by car
#method speed
#call start and speed
#sports car object


class Vechile:
    def start(self):
        print("Vechile started")

class Car(Vechile):
   pass

class Sportscar(Car):
    def speed(self):
        print("Sportscar speed is 100")

sp = Sportscar()
sp.start()
sp.speed()


#problem4:
#employee skills
#create class programmer coding
#than class designig method
#than finally create a child class employee
#inhertance both class
#object of

          
          

class Programmer:
    def coder(self):
        print("Programmer creates code")

class Designer(Programmer):
    def design(self):
        print("Designer creates designs")

class Employee(Designer):
    pass

e1 = Employee()
e1.coder()
e1.design()





class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return 0


class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.35      

n = int(input())
Employee = []
for i in range(n):
    role, name, salary = input().split()
    salary = float(salary)

    if role.lower() == "developer":
        emp = Developer(name, salary)
    elif role.lower() == "manager":
        emp = Manager(name, salary)

    print(f"Name:{emp.name}")
    print(f"Role:{role}")
    print(f"Bonus:{emp.calculate_bonus():.2f}")





#problem5



class Course:
    def _init_(self, student_name):
        self.student_name = student_name

    def access_level(self):
        pass


class FreeCourse(Course):
    def access_level(self):
        return "Limited Access"


class PremiumCourse(Course):
    def access_level(self):
        return "Full Access"


n = int(input())
Students = []

for _ in range(n):
    course_type, student_name = input().split()

    if course_type == "Free":
        student = FreeCourse(student_name)
    else:
        student = PremiumCourse(student_name)
Student.append((obj,course_type))
for obj, course_type in students:
    print(f"Student:{student.student_name}")
    print(f"Course_type:{course_type}")
    print(f"Access:{student.access_level()}")  
      