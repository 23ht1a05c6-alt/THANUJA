file = open("student.txt", "a")

name = input("Enter a name: ")

file.write(name + "\n")

file.close()

print("Data appended successfully")




file = open("student.txt", "r")

line = file.readline()

print(line)

file.close()



file = open("hello.txt", "r")

line = file.readline()

print(line)

file.close()



file = open("hello.txt", "r")

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()

print(line1)
print(line2)
print(line3)

file.close()
#read lines convert into list



# retur#ns correct cruser pointer method 

