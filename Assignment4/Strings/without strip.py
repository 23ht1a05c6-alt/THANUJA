s = input("Enter a string: ")

# Remove leading spaces
start = 0
while start < len(s) and s[start] == " ":
    start += 1