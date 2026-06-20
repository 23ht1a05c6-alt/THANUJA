class Student:
    def __init__(self,name,marks):
        self,__name = name
        self.__marks = marks
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks 
    def Calculate_grade(self):
        pass
class Undergraduate(Student):
    def Calculate_grade(self):
        marks = self.get_marks()
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"
class Postgraduate(Student);
            


 

   
    