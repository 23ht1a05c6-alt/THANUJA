
nums = [10, 20, 30]
for num in nums:
    print(num)



    nums = [10, 20, 30, 40]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
print(next(it))




#stop iteration
nums = [10, 20]

it = iter(nums)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # StopIteration




nums = [10, 20, 30]

it = iter(nums)

for x in it:
    print(x)






