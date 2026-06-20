arr = [90, 80, 90, 70, 80, 90]

d = {}

for num in arr:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

print(d)









n = int(input())
fruits = input().split()

unique_fruits = sorted(set(fruits))                      
print(*unique_fruits)






arr 1 ={1,2,3,4,5}
arr 2 ={3,4,5,6,7}
print(arr 1 & arr 2)





