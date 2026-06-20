try:
    with open("filehandlingbasics.py", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")




with open("student.txt", "w") as file:
    file.write("Name: Tanu\n")
    file.write("Course: Python")
# if there is a file delate old dta and add new contebt



with open("readfile.py", "r") as source:
    data = source.read()

with open("filehandlingbasics.py", "w") as target:
    target.write(data)

print("File copied successfully")



#append mode
''''''
file = open("sample.txt", "a")
file.write("Hello Python")
file.close()

''''''



with open("student.txt", "a") as file:
    file.write("\nAnjali")

print("Data appended successfully")