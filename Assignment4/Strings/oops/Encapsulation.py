#encapuslation is aytherised
#data is hidden inside it similarly data is hidden acess useing methods
#key idea
#combine data into singal unit by mixing the data and methods
#features
#control acess(limited acess)
#security
#data hiding
#controlled access
#better maintance




class BankAccount:
    def __init__(self, start_money):
        self.__balance = start_money  # __ makes it private (hidden)

    def deposit(self, amount):
        self.__balance += amount  # Adds money safely

    def get_balance(self):
        return self.__balance  # Shows money safely


# --- Running the program ---
account = BankAccount(100)  # Start with $100
account.deposit(50)  # Add $50

print("Balance:", account.get_balance())  # Prints 150








#data hiding
#the simple goal is to prevnt the modifications
#to prvent the misuse of dta
#access modifier
#public
#private
#protect

#public:
#data can be access in any where
#if we donnot specfic any data modifier they can perfraom public only

#protect keep_
#private keep__
#piblic underscore




class BankAccount:
    def __init__(self, name, balance):
        self.name = name              # Public variable
        self._balance = balance       # Protected variable
        self.__pin = 1234             # Private variable

    # Public method
    def show_details(self):
        print("Name:", self.name)
        print("Balance:", self._balance)

    # Private data access via method
    def get_pin(self):
        return self.__pin

    def set_balance(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Invalid amount")


# Object creation
acc = BankAccount("Tanu", 5000)

# Public access
print(acc.name)

# Protected access (possible but not recommended)
print(acc._balance)

# Private access (not directly possible)
# print(acc.__pin) ❌ error

# Correct way to access private data
print("PIN:", acc.get_pin())
acc.set_balance(2000)
acc.show_details()


#why protect?
#during inhertance and 
#private is maore secure than compare product
#we can uses__
#uses for strong cata hiding
#private variable can access outsde of class
#name mangeling
#use of nae mangling
#accedental privant
#with in same class
#try to access name manging


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

s1 = Student("Rahul", 85)

s1.display()
# Accessing private variable using name mangling
print("Marks:", s1._Student__marks)


        
    

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.__balance)


acc = BankAccount(1000)

acc.check_balance()
acc.deposit(500)
acc.withdraw(300)
acc.check_balance() 



# getters for read the data
# setters can modified the data(update the data)


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    # Getter Method
    def get_balance(self):
        return self.__balance

    # Setter Method
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative")

acc = BankAccount(1000)

print("Balance:", acc.get_balance())

acc.set_balance(2000)
print("Updated Balance:", acc.get_balance())




class Student:
    def __init__(self, marks):
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

s = Student(80)

print("Marks:", s.get_marks())

s.set_marks(95)
print("Updated Marks:", s.get_marks())




class Student:
    def __init__(self, marks):
        self.__marks = marks

    # Getter
    @property
    def marks(self):
        return self.__marks

    # Setter
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid Marks")
values = int(input())
s = Student(80)
print("Marks:", s.marks)   # Getter

s.marks = 95              # Setter
print("Updated Marks:", s.marks)
        



class Employee:
    def __init__(self, salary):
        self.__salary = salary      # private variable

    def increase_salary(self, percentage):
        if self.__salary <= 0:
            print("Invalid Salary")
        else:
            self.__salary += self.__salary * percentage / 100

    def get_salary(self):
        return self.__salary


salary = int(input("Enter Salary: "))
percentage = int(input("Enter Increase Percentage: "))

emp = Employee(salary)
emp.increase_salary(percentage)

print("Updated Salary:", emp.get_salary())





class Password
