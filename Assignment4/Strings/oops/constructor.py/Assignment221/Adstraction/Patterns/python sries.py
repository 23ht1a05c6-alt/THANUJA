n = 10
for i in range(1,11):
    for j in range(i):
        print("*" ,end="")
    print(" ") 



#hallow square
n = 7
print("* " * n)
for i in range(n-2):
    print("* "+" "*(n-2)+"  *")
print("* " * n)

   

for i in range(6):
    for j in range(7):
        if(i==0 and  j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print("*", end="")
        else:    
            print(end="")
print()        
            

