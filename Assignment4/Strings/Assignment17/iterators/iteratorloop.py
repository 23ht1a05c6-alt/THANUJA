nums = [10, 20, 30]

it = iter(nums)

for x in it:
    print(x)



nums = [2,3,4]
it = iter(nums)



name = "python" 
it = iter(name)





name = "python"
it = iter(name)
print(next(it))  # p
print(next(it))  # y
print(next(it))  # t
print(next(it))  # h
print(next(it))  # o
print(next(it))  # n






name = "python"
it = iter(name)
print(it)





t = [1, 2, 3]
it = iter(t)
print(it)









d = {
    a = 10
    b = 20
}
b = 20
it = iter(b)
print(next(it))




d = {
    "name": "Tanu",
    "age": 20,
    "city": "Guntur"
}

it = iter(d)

print(next(it))
print(next(it))
print(next(it))





#creating custom iterator
#count iterator



class CountIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

obj = CountIterator(5)

for num in obj:
    print(num)