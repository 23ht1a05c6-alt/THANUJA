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







''''''



arr = [-2,4,5,3 ,2]
current_max = arr[0]
current_min = arr[0]
max_product = arr[0]





