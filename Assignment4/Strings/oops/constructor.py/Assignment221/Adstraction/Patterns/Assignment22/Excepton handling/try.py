try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input")



#we can say cannot divide wth zero
# when 10/0 above words will be comeing
# alphbat  will come error 
# value error
# so input sholud not be string
#  common  python exception
# Zero Division Error

#   Value Error 
# Type Error : wrong dta type
# Index Error:we can pause invalid syntax

#  Key Error:invalid dictory when we can pause
# fill not found:
#attribute Error:Invaid Atribute
# Name Error:wheb we nt defined we will get




try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")  



#first exceptin is index eror print out of range



#ValueErro
try:
    num = int("abc")
except ValueError:
    print("Invalid value")


#IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")  



#IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")    



#5. NameError
try:
    print(x)
except NameError:
    print("Variable is not defined")




##if no exception than lse block will be excuted
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)




# final key word
# finally block excutes always
# used throgh close files
# data base 
# clen up activitices
# they will come exception are not they will be come finaloutput

    

try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input")
finally:
    print("Program ended")





try:
    num = int(input("Enter the transcation"))
    print(num)
except ValueError:
    print(("tranaction is process")
finally:
    pass("transactuin")

#nested try catch blocks
import try:
num = int(input())



#nsted id can be used in try catch nlocks can be usw



#rase  can used in manuvaliy used to geberate
int age = ("enter the the age")
if age<18:b
   rise exception  
age > 18
   



custem exception why
'''''

'class MyException:

    pass
class Insufficient_balance:
    
    
 balance = 5000
print(suminput()'enter the balance)
  
 

# oops wit exception handling
#  student result system
# 
# 
#   



class Studentmarks:
     self.marks = marks
avd = sum(self.,arks) 
print('avgerage)
     pass

              

     
class BankBalance:
    self.balabce = balance
    self.amount = amount
      pass
try:
balance = 50000
print(ban balance)    




#login system 


class loginsystems;
    if ()
    rise:
#except accont is negative dily limit 2500
#splay remaining balance



class Balance:
    self.balance = balance
    self.withdraw = withdraw
       pass
bank_balance - = withdraw
print("withdraw amount
       


try:
    # risky code
except:
    # handle exception
else:
    # executes if no exception
finally:
    # always executes



try:
    age = int(input("Enter age: "))
    print("Age:", age)

except ValueError:
    print("Please enter numbers only")