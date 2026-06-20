





n = int(input())
height = list(map(int, input().split()))

left = [0] * n
right = [0] * n

left[0] = height[0]
for i in range(1, n):
    left[i] = max(left[i - 1], height[i])

right[n - 1] = height[n - 1]
for i in range(n - 2, -1, -1):
    right[i] = max(right[i + 1], height[i])

water = 0

for i in range(n):
    water += min(left[i], right[i]) - height[i]

print(water)






n = int(input())
height = list(map(int, input().split()))

left = 0
right = n - 1

left_max = 0
right_max = 0
water = 0

while left <= right:

    if height[left] <= height[right]:

        if height[left] >= left_max:
            left_max = height[left]
        else:
            water += left_max - height[left]

        left += 1

    else:

        if height[right] >= right_max:
            right_max = height[right]
        else:
            water += right_max - height[right]

        right -= 1

print(water)








