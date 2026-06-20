class Student:
    collage = "CITY engineering collage"
    def __init__(self, name):
        self.name = name
s1 = Student("Tanu") 
s2 = Student("mounika") 
print(s1.name) 




class Student:
    collage = "CITy engineering collage"#class variable
    def __init__(self, name,rolno):
        self.name = name#instances variable
        self.branch = rolno#instances variable
        
    def display(self):
        print("Student Name":, self.name)
        print("roll Number": self.rollno)
        print("collage Name:", Student . collage)    
s1 = Student("Tanu", 90 ) 
s2 = Student("mounika", 80 ) 
s1.display()
print()
s2.display()

        


 
    
        