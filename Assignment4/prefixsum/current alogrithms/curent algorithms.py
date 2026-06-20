f#ind the continous sub array  max
arr = [2,-1,]






 arr = [1, 2, 3, 4]

prefix = [0] * len(arr)
prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

# sum L to R
L, R = 1, 3
ans = prefix[R] - prefix[L-1] if L > 0 else prefix[R]
print(ans)






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


