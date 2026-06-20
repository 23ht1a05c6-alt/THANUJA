file = open("hello.txt", "r")

print("Current Position:", file.tell())

file.seek(6)

print("New Position:", file.tell())

print(file.read())

file.close()



file = open("hello.txt", "r")
file.seek(6)
print(file.read())
file.close()

#with open method
syntax:
with open("filename.txt", "mode") as file:
    # file operations



   
   

