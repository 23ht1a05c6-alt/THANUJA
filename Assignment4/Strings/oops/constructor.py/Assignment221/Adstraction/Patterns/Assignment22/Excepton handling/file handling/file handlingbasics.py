'''
file handling 
files helpsto store data parmentaly
file handling is a process of first creating files than we can write files reading files 
updateing File 
why file handling appers after the programming with files we an stor data parmental data sharing is possible
types of file
.tht
.jpg
text type of files
.csp
.jsn
*binary files(images,videos,pdf) 
your topic is opening file
syntax;
file = open("sample.txt", "r")
'''


file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()



file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()


#append file
file = open("sample.txt", "r")
data = file.read()
print(data)
file.close()



'''

| Mode | Meaning                                               |
| ---- | ----------------------------------------------------- |
| `r`  | Read only                                             |
| `w`  | Write only (creates file or overwrites existing file) |
| `a`  | Append (adds data at end of file)                     |
| `r+` | Read and Write                                        |
| `w+` | Write and Read (overwrites file)                      |
| `a+` | Append and Read                                       |
| `rb` | Read Binary                                           |
| `wb` | Write Binary                                          |

'''




#(Read)
with open("sample.txt", "r") as file:
    print(file.read())
#2. w (Write)
with open("sample.txt", "w") as file:
    file.write("Hello")

#3. a (Append)
with open("sample.txt", "a") as file:
    file.write("\nWelcome")

#a+ (Append and Read)
with open("sample.txt", "a+") as file:
    file.write("\nPython")
    file.seek(0)
    print(file.read())




5#. rb (Read Binary)  
with open("image.jpg", "rb") as file:
    data = file.read()
    print(data)  