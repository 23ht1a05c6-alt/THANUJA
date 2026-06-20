
student = {
    "id": 101,
    "name": "Tanu",
    "marks": 95
}

print(student)




student = dict(id=101, name="Tanu", marks=95)

print(student)



#deiate
student = {"name": "Tanu", "age": 22, "city": "Vijayawada"}

del student["age"]

print(student)






#update update muliple elements a a time
student = {"name": "Tanu", "age": 22}

student.update({"city": "Vijayawada"})

print(student)





#pop item removes last insert pair
student = {"name": "Tanu", "age": 22}

student.pop("age"})

print(student)




student = {
    "name": "Tanu",
    "age": 22,
    "city": "Vijayawada"
}

item = student.popitem()

print(item)
print(student)





d = {'a': 1, 'b': 2, 'c': 3}

print(d.popitem())
print(d)





student = {
    "name": "Tanu",
    "age": 22,
    "city": "Vijayawada"
}

print(student.items())





#nested dictory
students = {
    101: {"name": "Tanu", "age": 22},
    102: {"name": "Ravi", "age": 23}
}

print(students)






nums = [1, 2, 3, 2, 4, 1, 5]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

for key, value in freq.items():
    if value > 1:
        print(key)