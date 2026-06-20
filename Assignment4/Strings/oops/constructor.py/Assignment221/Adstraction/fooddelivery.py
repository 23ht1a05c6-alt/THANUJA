#wer

#In Python, dunder methods (short for "double underscore methods") are special methods whose names begin and end with double underscores, such as:
#__init__
#__str__
#__len__
#__add_


class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")


#__str__ – String Representation
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person({self.name})"

p = Person("Alice")
print(p)




#__len__ – Length
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

obj = MyList([1, 2, 3])
print(len(obj))



#__add__ – Addition Operator
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

n1 = Number(5)
n2 = Number(3)

result = n1 + n2
print(result.value)



'''| Operation      | Dunder Method |
| -------------- | ------------- |
| `obj + other`  | `__add__`     |
| `obj - other`  | `__sub__`     |
| `len(obj)`     | `__len__`     |
| `print(obj)`   | `__str__`     |
| `obj[index]`   | `__getitem__` |
| `obj == other` | `__eq__`      |
| `for x in obj` | `__iter__`    |''''




