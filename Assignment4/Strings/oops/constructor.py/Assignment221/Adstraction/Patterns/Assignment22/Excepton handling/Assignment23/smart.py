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