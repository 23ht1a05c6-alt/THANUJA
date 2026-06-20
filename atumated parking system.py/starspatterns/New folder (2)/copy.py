student = {
    "name": "Tanu",
    "age": 22
}

new_student = student.copy()

print(new_student)




#dictory why faster
d1 = {"a": 1, "b": 2}
d2 = d1

d2["a"] = 100

print(d1)
print(d2)






create  dictory with employee details know add branch and phone number
than key and values useing loop pop the last ordered PendingDeprecationWarning
make sure to copy before deiating know finaly to print make the employee in mulitple dictory know print the values
useing looping know each employee tas ha araay





# Multiple employees (nested dictionary)
employees = {
    101: {"name": "Tanu", "salary": 50000},
    102: {"name": "Ravi", "salary": 60000},
    103: {"name": "Priya", "salary": 55000}
}

# Add branch and phone number
for emp in employees.values():
    emp["branch"] = "Hyderabad"
    emp["phone"] = "9876543210"

# Print keys and values using loops
print("Employee Details:")
for emp_id, details in employees.items():
    print("\nEmployee ID:", emp_id)
    for key, value in details.items():
        print(key, ":", value)

# Make a copy before deleting
employees_copy = employees.copy()

# Remove last inserted employee
removed = employees_copy.popitem()

print("\nRemoved Employee:")
print(removed)

# Final dictionary
print("\nRemaining Employees:")
for emp_id, details in employees_copy.items():
    print("\nEmployee ID:", emp_id)
    for key, value in details.items():
        print(key, ":", value)