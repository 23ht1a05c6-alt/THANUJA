# Write student marks into a file

with open("marks.txt", "w") as file:
    for i in range(3):
        mark = input(f"Enter marks of Student {i+1}: ")
        file.write(mark + "\n")

print("Marks saved successfully")





with open("marks.txt", "r") as file:
    print("Student Marks:")
    
    for line in file:
        print(line.strip())




with open("withopen.py", "w") as file:
    for i in range(3):
        name = input("Enter Student Name: ")
        marks = input("Enter Student Marks: ")

        file.write(name + " " + marks + "\n")

print("Data stored successfully")




with open("employee.txt", "w") as file:
    for i in range(3):
        name = input("Enter Employee Name: ")
        salary = input("Enter Employee Salary: ")

        file.write(name + " " + salary + "\n")

print("Employee details stored successfully")




with open("employee.txt", "r") as source:
    data = source.read()

with open("backup.txt", "w") as target:
    target.write(data)

print("Data copied successfully")



