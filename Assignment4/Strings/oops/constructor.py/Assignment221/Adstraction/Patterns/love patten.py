for i in range(6):
    for j in range(7):
        if((i == 0 and  j % 3 !=0) or (i == 1 and j % 3 == 0) or (i-j == 2) or (i + j == 8)):
            print("*", end=" ")
        else:    
            print(" ", end=" ")
    print()




n = 5
#roof
for i in range(n):
    print(" " * (n - i - 1) + "H" * (2 * i + 1))
#huse body
for i in range(n):
    print("O" + " " * (2 * n - 3) + "O")




3roof
for i in range(1,5):
    print(" " * (4 - i) + "" * (2 * i- 1))
#house body
for i in range(3):
    print("|    |") 
#base
print("|_____|")       
