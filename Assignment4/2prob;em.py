n = int(input())
arr = list(map(int, input().split()))

max_prod = arr[0]
min_prod = arr[0]
result = arr[0]

for i in range(1, n):
    if arr[i] < 0:
        max_prod, min_prod = min_prod, max_prod

    max_prod = max(arr[i], max_prod * arr[i])
    min_prod = min(arr[i], min_prod * arr[i])

    result = max(result, max_prod)

print(result)







employee = {
    "name":"tanu,"
    "marks":95
    print(employee)
} 





nums = [1, 2, 3, 2, 4, 1, 5]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

for key, value in freq.items():
    if value > 1:
        print(key)
