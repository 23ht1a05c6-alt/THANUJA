






dict = "apple banana strawberry pineapple apple banana"

freq = {}

for word in dict.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)





freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)




text =  "apple banana strawberry pineapple apple banana"
word = text.split()
freq = {}





#copy
student = {
    "name": "Tanu",
    "age": 22
}

new_student = student.copy()

print(new_student)





d1 = {"a": 1, "b": 2}
d2 = d1

d2["a"] = 100

print(d1)



