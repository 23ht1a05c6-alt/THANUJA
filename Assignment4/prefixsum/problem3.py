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






  