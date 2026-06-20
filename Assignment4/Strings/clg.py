my_string = "Hello World"
count = 0

for char in my_string:
    count += 1

print("Length of the string is:", count)


  

S = "hello"
print(S.lower case())




string = input("Enter the string")
rsult =""
for ch in string:
    if ch. lower() not in ['a','e','i','o','u']:
        result = result+ch
print(result)
        




string = "hello"hex
for ch in string
    if ch.
result = result + string
print(string.capitalize)





# String with extra spaces and newlines
text = "  \n  Clean this text!  \t  "

# Using strip() with no arguments defaults to whitespace
cleaned_text = text.strip()

print(f"Original: '{text}'")
print(f"Cleaned:  '{cleaned_text}'")



# Without using strip() function

s = input("Enter a string: ")

# Remove leading spaces
start = 0
while start < len(s) and s[start] == " ":
    start += 1

# Remove trailing spaces
end = len(s) - 1
while end >= 0 and s[end] == " ":
    end -= 1

# Create new string
result = ""
for i in range(start, end + 1):
    result += s[i]

print("String after removing spaces:", result)




s = input("enter the string")
result=""
for ch in s:
  if ch !=" ":
      result=result+ch
print("output" result)








char_a = 'A'
ascii_a = ord(char_a)
print(ascii_a)
















num = int(input("give 1st number:"))
num = int(input("give 2st number:"))
operator = input("give operator:")
if operator == "+":
    print(f"addition of 2 numbers is {num1+num2} ")
elif operator == "-":
    print(f"subtraction of 2 numbers is {num1-num2} ") 
elif operator == "*":
    print(f"multpication of 2 numbers is {num1*num2} ") 
elif operator == "/":
     print(f"division of 2 numbers is {num1/num2} ") 
else:
    print("not vaild")
