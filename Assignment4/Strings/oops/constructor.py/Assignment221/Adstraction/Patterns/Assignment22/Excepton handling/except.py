try:
    age = int(input("Enter age: "))
    print("Age:", age)

except ValueError:
    print("Please enter numbers only")





class Employee:
    def __init__(self, emp_id, name, skills):
        self.emp_id = emp_id
        self.name = name
        self.skills = list(set(skills))

n = int(input())

employees = []
all_skills = set()

for i in range(n):
    emp_id = int(input())
    name = input()
    skills = input().split(",")

    emp = Employee(emp_id, name, skills)
    employees.append(emp)

    all_skills.update(emp.skills)

print("Unique Skills Count:", len(all_skills))

max_emp = max(employees, key=lambda x: len(x.skills))
print("Employee with Max Skills:", max_emp.name)

print("Employees Knowing Python:")
for emp in employees:
    if "Python" in emp.skills:
        print(emp.name)





'''''
marks of five subjects  marks should negative zero and 100
avg >= 75 grade a
avg >=  60 grade break
avg >= 40 pass

'''''



# Student Result Processing using Exception Handling
class NegativeMarksError(Exception):
    pass

class MarksExceedError(Exception):
    pass



class StudentResult:

    def __init__(self):
        self.marks = []

    def get_marks(self):
        for i in range(5):
            try:
                mark = float(input(f"Enter marks of Student {i+1}: "))

                if mark < 0:
                    raise NegativeMarksError("Marks cannot be negative")

                if mark > 100:
                    raise MarksExceedError("Marks cannot exceed 100")

                self.marks.append(mark)

            except ValueError:
                print("Error: Non-numeric input is not allowed")
                return False

            except NegativeMarksError as e:
                print("Error:", e)
                return False

            except MarksExceedError as e:
                print("Error:", e)
                return False

        return True

    def calculate_result(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 75:
            grade = "Distinction"
        elif avg >= 60:
            grade = "First Class"
        elif avg >= 40:
            grade = "Pass"
        else:
            grade = "Fail"

        print("\nAverage:", avg)
        print("Grade:", grade)
obj = StudentResult()
if obj.get_marks():
    obj.calculate_result()




try:
    age = int(input("Enter age: "))
    print("Age:", age)

except ValueError:
    print("Please enter numbers only")





try:
    age = int(input("Enter age: "))
    print("Age:", age)

except ValueError:
    print("Please enter numbers only")




