



def simple_interest(p, t, r):
    return (p * t * r) / 100

si = simple_interest(1000, 2, 5)
print("Simple Interest =", si)




#keyword arguments a=



#ex:
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=21, name="Tanu")




def simple_interest(p, t, r):
    return (p * t * r) / 100

si = simple_interest(p=1000, t=2, r=5)
print("Simple Interest =", si)




# 3 type default argument
#constant values 
#used when value is not provided



#create a function to caluate default function square




def simple_interest(p=1000, t=1, r=5):
    return (p * t * r) / 100

print(simple_interest())        # Uses default values
print(simple_interest(2000))    # p = 2000, t and r use defaults



def greet(name="Guest"):
    print("Hello", name)

greet()          # Uses default value
greet("Tanu")    # Uses provided value





#default  arument
def square(a,b=2):
    print(a**b)
square(10)




#variable length argument
#ex; crate a function sum of any number of value






def find_sum(*args):
    print(args)

find_sum(10, 20, 30)




c##reate a  employee details y useing quade





def employee_details(**kwargs):
    print(kwargs)
employee_details(name="Tanu", age=21)




def add(*args):
    print(args)
    print("Sum =", sum(args))

add(10, 20, 30, 40)





def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(find_sum(10, 20, 30))