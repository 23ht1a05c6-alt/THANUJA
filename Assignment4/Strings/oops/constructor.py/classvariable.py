#class variable instances class  show method
class Student:
    # Class Variable
    school_name = "ABC School"

    def __init__(self, name, age):
        # Instance Variables
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school_name)       
# Creating Objects
s1 = Student("Tanu", 21)
s2 = Student("Rahul", 22)

# Calling show() method
s1.show()
print("-----")
s2.show()

    

#class method

class ClassName:

    @classmethod
    def method_name(cls):
        # class variable access
        pass




class Employee:
    company = "Infosys"   # Class Variable

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

# Before changing
print("Company:", Employee.company)

# Calling class method
Employee.change_company("TCS")

# After changing
print("Company:", Employee.company)




class College:
    college_name = "CITY Engineering College"   # Class Variable

    def __init__(self, student_name, branch):
        self.student_name = student_name       # Instance Variable
        self.branch = branch

    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    def show(self):
        print("Student Name:", self.student_name)
        print("Branch:", self.branch)
        print("College:", College.college_name)


# Creating Objects
s1 = College("Tanu", "CSE")
s2 = College("Rahul", "ECE")

print("Before changing college name:")
s1.show()
print()
s2.show()

# Calling Class Method
College.change_college("XYZ Engineering College")

print("\nAfter changing college name:")
s1.show()
print()
s2.show()
#decartoe use for class not for objecy
#cls is current class



#create a class named as employee create sum 
#use class mehod by applying on copany  name useing multiple object




# Create a class named Employee

class Employee:
    company_name = "Infosys"   # Class Variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    def show(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)
        print()


# Multiple Objects
e1 = Employee("Tanu", 50000)
e2 = Employee("Rahul", 60000)
e3 = Employee("Kiran", 70000)

print("Before changing company name:")
e1.show()
e2.show()
e3.show()

# Class Method
Employee.change_company("TCS")

print("After changing company name:")
e1.show()
e2.show()
e3.show()




class Employee:
    company_name = "Infosys"   # Class Variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)
        print()
# Multiple Objects
e1 = Employee("Tanu", 50000)
e2 = Employee("Rahul", 60000)
e3 = Employee("Kiran", 70000)

print("Before changing company name:")
e1.show()
e2.show()
e3.show()

# Changing class variable directly
Employee.company_name = "TCS"

print("After changing company name:")
e1.show()
e2.show()
e3.show()





class Employee:
    company_name = "Infosys"   # Class Variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    def show(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)
        print()


# Creating Multiple Objects
e1 = Employee("Tanu", 50000)
e2 = Employee("Rahul", 60000)
e3 = Employee("Kiran", 70000)

print("Before Changing Company:")
e1.show()
e2.show()
e3.show()

# Calling Class Method
Employee.change_company("TCS")

print("After Changing Company:")
e1.show()
e2.show()
e3.show()




#differebce between instances method and class method
#instances method works onobject data
#uses for self referes to current object
#acess the instances varianles
#class method works on clas data
#uses the cls referes to class
#acess the



#by ueing instances method and class method


class Employee:
    company = "Infosys"

    def __init__(self, name):
        self.name = name

    def show(self):      # Instance Method
        print(self.name, Employee.company)

    @classmethod
    def change_company(cls, cname):   # Class Method
        cls.company = cname


e1 = Employee("Tanu")
e2 = Employee("Rahul")

e1.show()
e2.show()

Employee.change_company("TCS")

e1.show()
e2.show()





#static method
#does not uses either object are either class
#@staticmethod is decarator


class Employee:

    @staticmethod
    def greet():
        print("Welcome to the Company")

Employee.greet()






class Calculator:

    @staticmethod
    def add(a, b):
        print("Sum =", a + b)
Calculator.add(10, 20)



#constuctor calss variablees instances variables instances method class method static method

# by useing Student





class Student:
    college = "CITY"#class variable
    def __init__(self, name,branch):
        self.name = name
        self.branch = branch #instances variable
    def show(self): #instances method
        print("Name:", self.name) 
        print("Branch:", self.branch)   
s1.Student = ("Tanu")
s2.Student = ("cse" )
#calling instances method
s1.show()
s2.show()  





class PasswordManager:
    def __init__(self, password):
        self.__password = password

    def set_password(self, password):
        if len(password) >= 8:
            self.__password = password
            print("Password Updated")
        else:
            print("Password must be at least 8 characters")

    def get_password(self):
        return self.__password


pm = PasswordManager("welcome123")

pm.set_password("python123")
print(pm.get_password())





class ShoppinCart:
    def __init__(self,cloths):
        self.__cloths = cloths
        
           

        
   