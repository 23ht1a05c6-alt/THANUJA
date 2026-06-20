class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand)
print(car2.brand)





limit = 5

for i in range(1, limit + 1):
    print(i)




class EvenIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 2
            return value
        raise StopIteration

obj = EvenIterator(10)

for num in obj:
    print(num)  



    create a custom iterator for even number   