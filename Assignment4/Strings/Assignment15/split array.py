n = int(input())
nums = list(map(int, input().split()))
k = int(input())

def can_split(nums, k, max_sum):
    count = 1
    curr_sum = 0

    for num in nums:
        if curr_sum + num > max_sum:
            count += 1
            curr_sum = num
        else:
            curr_sum += num

    return count <= k

low = max(nums)
high = sum(nums)

while low <= high:
    mid = (low + high) // 2

    if can_split(nums, k, mid):
        high = mid - 1
    else:
        low = mid + 1

print(low)






 




''''''''

n = int(input())

words = input().split()

d = {}

for word in words:
    key = "".join(sorted(word))

    if key not in d:
        d[key] = []

    d[key].append(word)

print(list(d.values()))






n = int(input())

d = {}

for _ in range(n):
    word = input().strip()

    key = "".join(sorted(word))

    if key not in d:
        d[key] = []

    d[key].append(word)

for group in d.values():
    print("[" + " ".join(group) + "]")




    | Feature      | Iterator                      | Generator                      | Decorator                     |
| ------------ | ----------------------------- | ------------------------------ | ----------------------------- |
| Purpose      | Traverse elements one by one  | Create iterators easily        | Modify behavior of functions  |
| Keyword Used | `__iter__()` and `__next__()` | `yield`                        | `@`                           |
| Memory Usage | Efficient                     | More efficient (lazy loading)  | Not related to memory         |
| Complexity   | More code                     | Less code                      | Used for function enhancement |
| Returns      | Next value using `next()`     | Generates values using `yield` | Returns a modified function   |
