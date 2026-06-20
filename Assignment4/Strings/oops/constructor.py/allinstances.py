
class Student:
    college = "CITY"#class variable
    def __init__(self, name,branch):
        self.name = name
        self.branch = branch #instances variable
    def show(self): #instances method
        print("Name:", self.name) 
        print("Branch:", self.branch)   
        print
s1 = Student("Tanu")
s2 = Student("cse")
#calling instances method
s1.show()
print()
s2.show()






#instances variable
class Student:
    def __init__(self,name,marks ):
        self.name = name
        self.marks = marks
s1 = Student("Tanu"90) 
s2 = Student("ratna",80) 
print(s1.name, s1.marks)
print(s2.name, s2.marks)






