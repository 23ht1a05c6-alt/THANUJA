#with out useing revrse string
s = "madam"
rev=""
for ch in  s:
         rev = ch + rev
if s == rev
   print("palindrome")
else:
   print("not palindrome")
