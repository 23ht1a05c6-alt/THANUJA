
s = input("enter the string")
result=""
for ch in s:
  if ch !=" ":
      result=result+ch
print(result)





s = input("enter the string")
result=""
for ch in s:
   if ch != {}[]():
      result = result + ch
print(result)






s = input("enter the string")
result=""
for ch in s:
   


s = "12abc20xy5"

num = ""
total = 0

for ch in s:
    if ch.isdigit():
        num = num + ch
    else:
        if num != "":
            total = total + int(num)
            num = ""

# last number check
if num != "":
    total = total + int(num)

print("Sum =", total)







s = input("Enter the string: ")

result = ""

for ch in s:
    if ch not in "{}[]()":
        result = result + ch

print(result)