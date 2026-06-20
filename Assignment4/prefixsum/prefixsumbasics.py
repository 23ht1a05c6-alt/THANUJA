



arr = [2, 4, 1, 3, 7]
result = sum(arr[1:4])
print(result)











arr = [2, 4, 1, 3, 7] 

result = sum(arr[1:4])   
print(result)














arr = [2,4,1,7,3]
L =1
R = 3
total = 4
for i in range(L-1,R): 
  total -= arr[i]
print(total)






]
rr = [2,4,1,7,3]
n = len(arr)
#create a prefix array 
prefix =[0]*n

#[0,0,0,0,0]
prefix[0] = arr[0]
#[2,0,0,0,0]
#build   the prefix sum
for i in range(1,n):
   prefix[i] = prefix[i-1]+arr[i]

print(prefix)
L = 1
R = 3
#range sum
if L == 0:
   answer = prefix[R]





arr = [2,4,1,7,3]
n = len(arr)
#create a prefix array 
prefix =[0]*n

#[0,0,0,0,0]
prefix[0] = arr[0]
#[2,0,0,0,0]
#build   the prefix sum
for i in range(1,n):
   prefix[i] = prefix[i-1]+arr[i]

print(prefix)
L = 1
R = 3
#range sum
if L == 0:
   answer = prefix[n]








arr = [2,4,1,7,3]
n = len(arr)

# Create prefix array
prefix = [0] * n

prefix[0] = arr[0]

# Build prefix sum
for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)   # [2, 6, 7, 14, 17]

L = 1
R = 3

# Range sum
if L == 0:
    answer = prefix[R]
else:
    answer = prefix[R] - prefix[L-1]

print(answer)







arr = [2,4,1,7,3]
n = len(arr)

prefix = [0] * n
prefix[0] = arr[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)

L = 1
R = 3

if L == 0:
    answer = prefix[R]
else:
    answer = prefix[R] - prefix[L-1]

print(answer)






arr = [1, 3, 5, 2, 2]
n = len(arr)

prefix = [0] * n
prefix[0] = arr[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]

total = prefix[-1]

for i in range(n):
    left_sum = prefix[i - 1] if i > 0 else 0
    right_sum = total - prefix[i]

    if left_sum == right_sum:
        print("Equilibrium Index:", i)
        break