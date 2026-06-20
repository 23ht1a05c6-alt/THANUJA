class Student:
    def __init__(self, name):
        self.name = name

    def display(self):      # Instance Method
        print("Name:", self.name)





class Student:
    school = "ABC School"      # Class Variable

    def __init__(self, name, marks):
        self.name = name       # Instance Variable
        self.marks = marks     # Instance Variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("School:", Student.school)

s1 = Student("Rahul", 85)
s2 = Student("Priya", 90)

s1.display()
print()
s2.display()





#normal method


class Student:
    school = "CITY College"      # Class Variable

    def __init__(self, name, marks):
        self.name = name       # Instance Variable
        self.marks = marks     # Instance Variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("College:", Student.college)

s1 = Student("Rahul", 85)
s2 = Student("Priya", 90)

s1.display()
print()

s2.display()


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

    


