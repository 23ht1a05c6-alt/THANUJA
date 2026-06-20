class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks
class ResultAnalayzer(Student):
    def get_average(self):
        marks = self.get_marks()
        return sum(marks) / len(marks)
    def count_passed_subjets(self):
        count = 0
        for mark in self.get_marks():
            if mark >= 50:
                count += 1
        return count
    def reverse_name(self):
        return self.get_name() [::-1]
name = input()
n = int(input())
marks = list(map(int, input().split()))
Student = ResultAnalayzer(name, marks)
print("Avarage Marks:")
round(Student.get_average(), 2)
print("Highest Mark:",Student.get_highest())
print("Passed Subjects:",Student.count_Passed_subjects())
print("Reversed Name:",Student.reverse_name())

          

