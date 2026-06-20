
num = int(input())
print("you enteed num",num, sep="")
          




t = (1, 2, 3, 4, 5, 6, 7, 8, 9, )
result = ()
for i in t:
    if i not in result:
        result += (i, )
print(result)        
    






t = (1, 2, 3, 2, 4, 1, 5)
result = tuple(set(t))
print(result)





a = input()
x,y,z = a.split(" ")
sum = int(x) + int(y) + int(z)
print(sum)




#exaple11
x,y = input('Enter name ad age:').split(" ,")
print("name;{x},age:{y}")


