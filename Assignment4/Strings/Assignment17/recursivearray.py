def product(arr, n):
    if n == 0:
        return 1
    return arr[n - 1] * product(arr, n - 1)

n = int(input())
arr = list(map(int, input().split()))
print(product(arr, n))






