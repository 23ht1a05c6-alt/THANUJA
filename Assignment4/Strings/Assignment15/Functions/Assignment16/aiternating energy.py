t = int(input())
for  _ in range(t):
   n = int(input())
   arr = list(map(int, input()).split())
   curr = float('_inf')
   max_sum = float('_inf')
   for i in range(n):
       val = arr[i]  if i % 2 == 0 else-arr[i]
       if curr < 0:
          curr = val
       else:
          curr = val
       max_sum = max(max_sum, curr)
print(max_sum)         
        

    


              
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    curr = float('-inf')
    max_sum = float('-inf')

    for i in range(n):
        val = arr[i] if i % 2 == 0 else -arr[i]

        if curr < 0:
            curr = val
        else:
            curr += val

        max_sum = max(max_sum, curr)

    print(max_sum)      