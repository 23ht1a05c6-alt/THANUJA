n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


'''
a company wants to generate employee details write a program except employe.txt calculate total salary 
expendictare finally we can display reprt
'''  



try:
    file = open("employee.txt", "r")

    total_salary = 0

    print("Employee Report")
    print("----------------")

    for line in file:
        name, salary = line.strip().split(",")
        salary = int(salary)

        print("Name:", name, "Salary:", salary)

        total_salary += salary

except FileNotFoundError:
    print("Error: employee.txt file not found")

except ValueError:
    print("Error: Invalid data in file")

finally:
    print("\nTotal Salary Expenditure:", total_salary if 'total_salary' in locals() else 0)
    print("Report Generated Successfully")
    try:
        file.close()
    except:
        pass


'''
Rahul,50000
Anjali,45000
Kiran,60000

Employee Report
----------------
Name: Rahul Salary: 50000
Name: Anjali Salary: 45000
Name: Kiran Salary: 60000

Total Salary Expenditure: 155000
Report Generated Successfully
'''



class Employee:

    def salary_report(self):
        try:
            file = open("employee.txt", "r")

            total_salary = 0

            print("Employee Details")
            print("----------------")

            for line in file:
                name, salary = line.strip().split(",")
                salary = int(salary)

                print("Name:", name, "Salary:", salary)
                total_salary += salary

        except FileNotFoundError:
            print("Employee file not found")

        except ValueError:
            print("Invalid data in file")

        finally:
            print("\nTotal Salary Expenditure:", total_salary if 'total_salary' in locals() else 0)
            print("Report Generated Successfully")

            try:
                file.close()
            except:
                pass


emp = Employee()
emp.salary_report()





Fibonacci Series – Brief Explanation

The Fibonacci Series is a sequence of numbers where each number is the sum of the previous two numbers.

Series:

0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Logic:

First number = 0
Second number = 1
Next number = Previous Number + Current Number

Example:

0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
Python Program
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
Sample Input
5
Output
0 1 1 2 3
Interview Answer (1 line)

Fibonacci series is a sequence in which each number is the sum of