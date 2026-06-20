arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

curr_sum = 0
max_sum = float('-inf')

for x in arr:
    curr_sum += x

    if curr_sum > max_sum:
        max_sum = curr_sum

    # reset if sum becomes negative
    if curr_sum < 0:
        curr_sum = 0

print("Max Sum:", max_sum)







arr = [2, -1, 3, -2, 4]

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    #either comtinue with old subarr
    #or start a new sub arr
    
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)
print("Maximum Subarray Sum =", max_sum)





arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print("Maximum Sum =", max_sum)






arr = [1, 2, 3]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        print(arr[i:j+1])





arr = [-2,4,-1,5,-3,2]
current_sum = arr[0]
max_sum = arr[0]
start = 0
end = 0
temp_start = 0
for i in range(1,len(arr)):

    #either starting a new sub array or extending
    if arr[i] > current_sum+arr[i]:
        current_sum = current_sum+arr[i]
    #new posible starting index
    temp_start = i
else:
    current_sum = current_sum+arr[i]
    #update the maximum
    if current_sum>max_sum:
        max_sum = current_sum
    ##save the index  values
    start  = temp_start
    end = i
print(max_sum)
print(start)
print(end)
print(arr[start:end+1])



''''''


#max of product values useing current algorithms
arr = [2, 3, -2, 4]

current_max = arr[0]
current_min = arr[0]
max_product = arr[0]

for num in arr[1:]:
    temp = current_max

    current_max = max(num,
                      current_max * num,
                      current_min * num)

    current_min = min(num,
                      temp * num,
                      current_min * num)

    max_product = max(max_product, current_max)

print(max_product)







arr = [-2,4,-1,5,-3,2]
current_sum = arr[0]
max_product = arr[0]
start = 0
end = 0
temp_start = 0
for i in range(1,len(arr)):

    #either starting a new sub array or extending
    if arr[i] > current_sum+arr[i]:
        current_sum = current_sum+arr[i]
    #new posible starting index
    temp_start = i
else:
    current_sum = current_sum+arr[i]
    #update the maximum
    if current_sum>max_product:
        max_product = current_sum
    ##save the index  values
    start  = temp_start
    end = i
print(max_sum)
print(start)
print(end)
