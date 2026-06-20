





#search a word in afile



word = input("Enter word to search: ")

with open("sample.txt", "r") as file:
    data = file.read()

if word in data:
    print("Word found")
else:
    print("Word not found")


 
with open("sample.txt", "r") as file:
    data = file.read()
count = len(data)
print("Number of characters:", count)





                      
