
s = input("Enter the string: ")

result = ""

for ch in s:
    if ch not in "{}[]()":
        result = result + ch
print(result)











s = input("enter the string")
result=""
for ch in s:
  if ch !=" ":
      result=result+ch
print(result)



s = "hello world"
print(s.split())


# Split string example
string = "hello world"
words = string.split()
print(words)






s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

# Compare sorted strings
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")






    s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")