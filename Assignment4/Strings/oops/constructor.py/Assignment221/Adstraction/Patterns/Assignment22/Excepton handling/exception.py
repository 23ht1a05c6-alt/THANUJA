| Error                                   | Exception                                           |
| --------------------------------------- | --------------------------------------------------- |
| Serious problem in the program.         | Runtime problem that can be handled.                |
| Usually cannot be handled easily.       | Can be handled using `try-except`.                  |
| Causes program termination.             | Program can continue after handling.                |
| Example: SyntaxError, IndentationError. | Example: ZeroDivisionError, ValueError, IndexError. |
#error and is a problem in the program causeing ubnormal
#syntax error
#run time error:can be handle by exception
#this run time error 
a = 10
b = 0
c = a/b
print(c)
#this will rise Exception
#logiacl error program runs but will come wrong output
#for ex:283+5
#ehat is exception handling
#''''exception handling is mechnasium run time error grase fully
#program will excute normaly
#basics exception handling
#basics  exception handling types
#try,catch, final,
#. ZeroDivisionError

#Occurs when a number is divided by zero.
a = 10
b = 0
print(a / b)

#try block 
#try:
   try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input")




#10/0 will be give in the input wll get zero divisble KeyError
#hides thactual program
#diffculy
