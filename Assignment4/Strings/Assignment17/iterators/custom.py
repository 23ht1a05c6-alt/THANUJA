class EvenNumbers:
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

# Create object
obj = EvenNumbers(10)

# Iterate using for loop
for num in obj:
    print(num)
if (slf.current )  