
#filter
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)





names = ["Anu", "Ravi", "Ajay", "Priya", "Arun"]

result = list(filter(lambda x: x.startswith("A"), names))

print(result)





#reduce it reduce the a singel value-
#from functools import reduce

#reduce(function, iterable)




from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)





from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]

result = reduce(add, numbers)

print(result)