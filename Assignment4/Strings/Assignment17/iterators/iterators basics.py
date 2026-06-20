#Iterators in Python

#An iterator is an object that allows you to traverse through all elements of a collection (like lists, tuples, etc.) one at a time.

#Key points:
#Implements two methods:
_#_iter__() → returns the iterator object
_#_next__() → returns the next value
#Raises StopIteration when done




nums = [1, 2, 3]

it = iter(nums)   # get iterator

print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3





class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

c = Counter(3)
for num in c:
    print(num)




#python references its memory effectence and control aess
#what is iterable?
# is an object can be looped
#{list,tuple,dictory,set,string}
e#x: i in range is iterable



'''''''



nums = [10, 20, 30]
for num in nums:
    print(num)





    ''''''''
iterable = [1, 2, 3, 4]

for item in iterable:
    print(item)